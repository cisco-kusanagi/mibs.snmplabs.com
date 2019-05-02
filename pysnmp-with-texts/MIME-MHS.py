#
# PySNMP MIB module MIME-MHS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIME-MHS
# Produced by pysmi-0.3.4 at Wed May  1 14:12:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, ModuleIdentity, Gauge32, Unsigned32, iso, MibIdentifier, Counter64, IpAddress, internet, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "ModuleIdentity", "Gauge32", "Unsigned32", "iso", "MibIdentifier", "Counter64", "IpAddress", "internet", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mail = MibIdentifier((1, 3, 6, 1, 7))
mime_mhs = MibIdentifier((1, 3, 6, 1, 7, 1)).setLabel("mime-mhs")
mime_mhs_headings = MibIdentifier((1, 3, 6, 1, 7, 1, 1)).setLabel("mime-mhs-headings")
id_hex_partial_message = MibIdentifier((1, 3, 6, 1, 7, 1, 1, 1)).setLabel("id-hex-partial-message")
id_hex_multipart_message = MibIdentifier((1, 3, 6, 1, 7, 1, 1, 2)).setLabel("id-hex-multipart-message")
mime_mhs_bodies = MibIdentifier((1, 3, 6, 1, 7, 1, 2)).setLabel("mime-mhs-bodies")
mibBuilder.exportSymbols("MIME-MHS", id_hex_multipart_message=id_hex_multipart_message, mime_mhs=mime_mhs, mime_mhs_bodies=mime_mhs_bodies, mime_mhs_headings=mime_mhs_headings, mail=mail, id_hex_partial_message=id_hex_partial_message)
