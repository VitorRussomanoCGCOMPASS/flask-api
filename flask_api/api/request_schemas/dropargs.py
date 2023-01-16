from marshmallow import fields, Schema, post_dump, RAISE


class DropSchema(Schema):

    class Meta:
        unknown =RAISE

    SKIP_VALUES = set([None])

    @post_dump
    def remove_skip_values(self, data, many, **kwargs):
        return {
            key: value for key, value in data.items() if value not in self.SKIP_VALUES
        }

