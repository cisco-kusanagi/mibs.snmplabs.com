#
# PySNMP MIB module BW-ClientManagementProfileServerFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-ClientManagementProfileServerFault
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
faultFields, severity, component, common, alarmState, subcomponent, recommendedActionsText, identifier, problemText, systemName, alarmName, timeStamp = mibBuilder.importSymbols("BroadworksFault", "faultFields", "severity", "component", "common", "alarmState", "subcomponent", "recommendedActionsText", "identifier", "problemText", "systemName", "alarmName", "timeStamp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Integer32, iso, Counter32, Gauge32, Unsigned32, IpAddress, TimeTicks, Counter64, NotificationType, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "iso", "Counter32", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2000-09-19 14:31',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200201220000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
bwPMClientManagementProfileServerLaunched = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5001)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerLaunched.setStatus('current')
bwPMClientManagementProfileServerShutDown = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5002)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerShutDown.setStatus('current')
bwPMClientManagementProfileServerRestarted = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5003)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerRestarted.setStatus('current')
bwPMClientManagementProfileServerServerDeath = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5004)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerServerDeath.setStatus('current')
mibBuilder.exportSymbols("BW-ClientManagementProfileServerFault", bwPMClientManagementProfileServerLaunched=bwPMClientManagementProfileServerLaunched, systemFaults=systemFaults, bwPMClientManagementProfileServerRestarted=bwPMClientManagementProfileServerRestarted, PYSNMP_MODULE_ID=systemFaults, bwPMClientManagementProfileServerShutDown=bwPMClientManagementProfileServerShutDown, bwPMClientManagementProfileServerServerDeath=bwPMClientManagementProfileServerServerDeath)
