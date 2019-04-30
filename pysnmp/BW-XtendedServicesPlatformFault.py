#
# PySNMP MIB module BW-XtendedServicesPlatformFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-XtendedServicesPlatformFault
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
faultFields, component, systemName, problemText, alarmName, identifier, common, severity, recommendedActionsText, alarmState, subcomponent, timeStamp = mibBuilder.importSymbols("BroadworksFault", "faultFields", "component", "systemName", "problemText", "alarmName", "identifier", "common", "severity", "recommendedActionsText", "alarmState", "subcomponent", "timeStamp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, Gauge32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, NotificationType, IpAddress, Counter64, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "NotificationType", "IpAddress", "Counter64", "TimeTicks", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2000-09-19 14:31',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200201220000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
bwXspTransactionGlobalRateLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 6001)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwXspTransactionGlobalRateLimitExceeded.setStatus('current')
bwXspTransactionUserRateLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 6002)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwXspTransactionUserRateLimitExceeded.setStatus('current')
mibBuilder.exportSymbols("BW-XtendedServicesPlatformFault", systemFaults=systemFaults, bwXspTransactionGlobalRateLimitExceeded=bwXspTransactionGlobalRateLimitExceeded, PYSNMP_MODULE_ID=systemFaults, bwXspTransactionUserRateLimitExceeded=bwXspTransactionUserRateLimitExceeded)
