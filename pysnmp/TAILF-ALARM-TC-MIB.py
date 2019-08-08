#
# PySNMP MIB module TAILF-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TAILF-ALARM-TC-MIB
# Produced by pysmi-0.3.4 at Wed Aug  7 20:00:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.7.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, IpAddress, ModuleIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Bits, MibIdentifier, ObjectIdentity, NotificationType, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "ModuleIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Bits", "MibIdentifier", "ObjectIdentity", "NotificationType", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tfModules, = mibBuilder.importSymbols("TAILF-TOP-MIB", "tfModules")
tfAlarmTCModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 24961, 2, 101))
tfAlarmTCModule.setRevisions(('2012-08-30 00:00', '2011-03-01 00:00',))
if mibBuilder.loadTexts: tfAlarmTCModule.setLastUpdated('201208300000Z')
if mibBuilder.loadTexts: tfAlarmTCModule.setOrganization('Tail-f Systems AB')
class TfAlarmIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class TfYANGResource(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TfAlarmOperatorState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("ack", 2), ("investigation", 3), ("observation", 4), ("closed", 5), ("other", 6))

class TfUtf8String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TfProbableCause(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("TAILF-ALARM-TC-MIB", TfYANGResource=TfYANGResource, PYSNMP_MODULE_ID=tfAlarmTCModule, TfAlarmIndex=TfAlarmIndex, TfAlarmOperatorState=TfAlarmOperatorState, TfProbableCause=TfProbableCause, tfAlarmTCModule=tfAlarmTCModule, TfUtf8String=TfUtf8String)
