#
# PySNMP MIB module TUBS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, enterprises, Integer32, TimeTicks, iso, MibIdentifier, Counter64, NotificationType, Unsigned32, ModuleIdentity, ObjectIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "enterprises", "Integer32", "TimeTicks", "iso", "MibIdentifier", "Counter64", "NotificationType", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tubs = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575))
tubs.setRevisions(('2002-07-01 15:00', '2002-05-16 15:00', '2000-02-09 00:00', '1997-02-14 10:23',))
if mibBuilder.loadTexts: tubs.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: tubs.setOrganization('TU Braunschweig')
ibr = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1))
if mibBuilder.loadTexts: ibr.setStatus('current')
ibrpib = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 10))
if mibBuilder.loadTexts: ibrpib.setStatus('current')
ibrpibtomib = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 11))
if mibBuilder.loadTexts: ibrpibtomib.setStatus('current')
ibrmibtopib = ObjectIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 12))
if mibBuilder.loadTexts: ibrmibtopib.setStatus('current')
class IBRUnsigned64(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class IBRInteger64(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

mibBuilder.exportSymbols("TUBS-SMI", ibrpib=ibrpib, ibrmibtopib=ibrmibtopib, IBRInteger64=IBRInteger64, ibrpibtomib=ibrpibtomib, PYSNMP_MODULE_ID=tubs, tubs=tubs, IBRUnsigned64=IBRUnsigned64, ibr=ibr)
