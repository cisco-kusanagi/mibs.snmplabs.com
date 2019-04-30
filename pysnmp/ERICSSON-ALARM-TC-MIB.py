#
# PySNMP MIB module ERICSSON-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERICSSON-ALARM-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:51:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ericssonModules, = mibBuilder.importSymbols("ERICSSON-TOP-MIB", "ericssonModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, IpAddress, Counter64, Integer32, iso, Counter32, NotificationType, MibIdentifier, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "Integer32", "iso", "Counter32", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ericssonAlarmTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 183, 3))
ericssonAlarmTCMIB.setRevisions(('2008-10-17 00:00',))
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setLastUpdated('200810170000Z')
if mibBuilder.loadTexts: ericssonAlarmTCMIB.setOrganization('Ericsson AB')
class EriAlarmType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class EriAlarmIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class EriAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 256)

class EriLargeAdditionalText(TextualConvention, OctetString):
    reference = 'snmpFrameworkMIB in RFC 3411 defines SnmpAdminString'
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 512)

class EriAlarmSpecificProblem(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 64)

class EriAlarmSequenceNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("ERICSSON-ALARM-TC-MIB", EriAdditionalText=EriAdditionalText, EriAlarmType=EriAlarmType, EriAlarmSequenceNumber=EriAlarmSequenceNumber, PYSNMP_MODULE_ID=ericssonAlarmTCMIB, EriLargeAdditionalText=EriLargeAdditionalText, EriAlarmSpecificProblem=EriAlarmSpecificProblem, ericssonAlarmTCMIB=ericssonAlarmTCMIB, EriAlarmIndex=EriAlarmIndex)
