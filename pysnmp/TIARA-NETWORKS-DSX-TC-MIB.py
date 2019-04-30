#
# PySNMP MIB module TIARA-NETWORKS-DSX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-DSX-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, TimeTicks, MibIdentifier, IpAddress, Gauge32, ObjectIdentity, Bits, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "TimeTicks", "MibIdentifier", "IpAddress", "Gauge32", "ObjectIdentity", "Bits", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tiaraMgmt, tiaraModules, tiaraInterfaces = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt", "tiaraModules", "tiaraInterfaces")
dsxTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 3, 2))
dsxTC.setRevisions(('1999-04-23 00:00',))
if mibBuilder.loadTexts: dsxTC.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: dsxTC.setOrganization('Tiara Networks Inc.')
class AlarmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class LEDState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("led-off", 1), ("led-green", 2), ("led-red", 3), ("led-yellow", 4), ("led-blinking-green", 5), ("led-blinking-red", 6), ("led-blinking-yellow", 7))

dsxMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 1))
dsxT1E1IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2))
dsxT3E3IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3))
mibBuilder.exportSymbols("TIARA-NETWORKS-DSX-TC-MIB", AlarmStatus=AlarmStatus, PYSNMP_MODULE_ID=dsxTC, dsxTC=dsxTC, dsxMIB=dsxMIB, dsxT3E3IfGroup=dsxT3E3IfGroup, LEDState=LEDState, dsxT1E1IfGroup=dsxT1E1IfGroup)
