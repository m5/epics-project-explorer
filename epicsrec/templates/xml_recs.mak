<response>
%for rec in c.recs:
	<rec name="${rec}">${rec}</rec>
%endfor
%for avail in c.avail:
	<avail name="${avail}">${avail}</avail>
%endfor
</response>
