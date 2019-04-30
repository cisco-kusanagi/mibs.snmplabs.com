#
# PySNMP MIB module DSX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DSX-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:39:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ntEnterpriseDataTasmanModules, ntEnterpriseDataTasmanMgmt, ntEnterpriseDataTasmanInterfaces = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanModules", "ntEnterpriseDataTasmanMgmt", "ntEnterpriseDataTasmanInterfaces")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, Counter64, Integer32, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Counter64", "Integer32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nndsxTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 3, 2))
nndsxTC.setRevisions(('1999-04-23 00:00',))
if mibBuilder.loadTexts: nndsxTC.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: nndsxTC.setOrganization('Nortel Networks')
class AlarmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class LEDState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("led-off", 1), ("led-green", 2), ("led-red", 3), ("led-yellow", 4), ("led-blinking-green", 5), ("led-blinking-red", 6), ("led-blinking-yellow", 7))

nndsxMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1))
nndsxT1E1IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2))
nndsxT3E3IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 3))
mibBuilder.exportSymbols("DSX-TC-MIB", nndsxTC=nndsxTC, LEDState=LEDState, AlarmStatus=AlarmStatus, nndsxT3E3IfGroup=nndsxT3E3IfGroup, nndsxT1E1IfGroup=nndsxT1E1IfGroup, PYSNMP_MODULE_ID=nndsxTC, nndsxMIB=nndsxMIB)
