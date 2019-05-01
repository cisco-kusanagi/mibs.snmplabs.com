#
# PySNMP MIB module BW-XtendedServicesPlatformFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-XtendedServicesPlatformFault
# Produced by pysmi-0.3.4 at Wed May  1 11:42:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
faultFields, component, systemName, subcomponent, problemText, timeStamp, severity, identifier, common, alarmName, alarmState, recommendedActionsText = mibBuilder.importSymbols("BroadworksFault", "faultFields", "component", "systemName", "subcomponent", "problemText", "timeStamp", "severity", "identifier", "common", "alarmName", "alarmState", "recommendedActionsText")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, MibIdentifier, Unsigned32, IpAddress, Counter32, Counter64, ModuleIdentity, TimeTicks, Gauge32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibIdentifier", "Unsigned32", "IpAddress", "Counter32", "Counter64", "ModuleIdentity", "TimeTicks", "Gauge32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2000-09-19 14:31',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: systemFaults.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200201220000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
if mibBuilder.loadTexts: systemFaults.setContactInfo('Broadsoft, Inc. 220 Perry Parkway Gaithersburg, MD 20877 301-977-9440')
if mibBuilder.loadTexts: systemFaults.setDescription('The defines the fault ')
bwXspTransactionGlobalRateLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 6001)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwXspTransactionGlobalRateLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: bwXspTransactionGlobalRateLimitExceeded.setDescription('Transaction denial due to high transaction rate for a given webapp.')
bwXspTransactionUserRateLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 6002)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwXspTransactionUserRateLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: bwXspTransactionUserRateLimitExceeded.setDescription('Transaction denial due to high transaction rate for a given userid.')
mibBuilder.exportSymbols("BW-XtendedServicesPlatformFault", systemFaults=systemFaults, bwXspTransactionUserRateLimitExceeded=bwXspTransactionUserRateLimitExceeded, bwXspTransactionGlobalRateLimitExceeded=bwXspTransactionGlobalRateLimitExceeded, PYSNMP_MODULE_ID=systemFaults)
