#
# PySNMP MIB module MIME-MHS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIME-MHS
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, iso, Counter64, ObjectIdentity, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Integer32, Counter32, MibIdentifier, TimeTicks, Bits, internet = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Counter64", "ObjectIdentity", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Integer32", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "internet")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mail = MibIdentifier((1, 3, 6, 1, 7))
mime_mhs = MibIdentifier((1, 3, 6, 1, 7, 1)).setLabel("mime-mhs")
mime_mhs_headings = MibIdentifier((1, 3, 6, 1, 7, 1, 1)).setLabel("mime-mhs-headings")
id_hex_partial_message = MibIdentifier((1, 3, 6, 1, 7, 1, 1, 1)).setLabel("id-hex-partial-message")
id_hex_multipart_message = MibIdentifier((1, 3, 6, 1, 7, 1, 1, 2)).setLabel("id-hex-multipart-message")
mime_mhs_bodies = MibIdentifier((1, 3, 6, 1, 7, 1, 2)).setLabel("mime-mhs-bodies")
mibBuilder.exportSymbols("MIME-MHS", mail=mail, mime_mhs_bodies=mime_mhs_bodies, mime_mhs_headings=mime_mhs_headings, id_hex_partial_message=id_hex_partial_message, mime_mhs=mime_mhs, id_hex_multipart_message=id_hex_multipart_message)
