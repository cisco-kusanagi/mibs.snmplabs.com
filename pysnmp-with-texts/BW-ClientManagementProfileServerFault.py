#
# PySNMP MIB module BW-ClientManagementProfileServerFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-ClientManagementProfileServerFault
# Produced by pysmi-0.3.4 at Wed May  1 11:42:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
identifier, component, subcomponent, systemName, alarmState, timeStamp, problemText, alarmName, recommendedActionsText, faultFields, common, severity = mibBuilder.importSymbols("BroadworksFault", "identifier", "component", "subcomponent", "systemName", "alarmState", "timeStamp", "problemText", "alarmName", "recommendedActionsText", "faultFields", "common", "severity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32, Bits, iso, TimeTicks, ObjectIdentity, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32", "Bits", "iso", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2000-09-19 14:31',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: systemFaults.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200201220000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
if mibBuilder.loadTexts: systemFaults.setContactInfo('Broadsoft, Inc. 220 Perry Parkway Gaithersburg, MD 20877 301-977-9440')
if mibBuilder.loadTexts: systemFaults.setDescription('The defines the fault ')
bwPMClientManagementProfileServerLaunched = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5001)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerLaunched.setStatus('current')
if mibBuilder.loadTexts: bwPMClientManagementProfileServerLaunched.setDescription('For the actual description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
bwPMClientManagementProfileServerShutDown = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5002)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerShutDown.setStatus('current')
if mibBuilder.loadTexts: bwPMClientManagementProfileServerShutDown.setDescription('For the actual description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
bwPMClientManagementProfileServerRestarted = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5003)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerRestarted.setStatus('current')
if mibBuilder.loadTexts: bwPMClientManagementProfileServerRestarted.setDescription('For the actual description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
bwPMClientManagementProfileServerServerDeath = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5004)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMClientManagementProfileServerServerDeath.setStatus('current')
if mibBuilder.loadTexts: bwPMClientManagementProfileServerServerDeath.setDescription('For the actual description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
mibBuilder.exportSymbols("BW-ClientManagementProfileServerFault", systemFaults=systemFaults, PYSNMP_MODULE_ID=systemFaults, bwPMClientManagementProfileServerShutDown=bwPMClientManagementProfileServerShutDown, bwPMClientManagementProfileServerRestarted=bwPMClientManagementProfileServerRestarted, bwPMClientManagementProfileServerServerDeath=bwPMClientManagementProfileServerServerDeath, bwPMClientManagementProfileServerLaunched=bwPMClientManagementProfileServerLaunched)
