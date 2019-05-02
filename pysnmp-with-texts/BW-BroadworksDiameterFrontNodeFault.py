#
# PySNMP MIB module BW-BroadworksDiameterFrontNodeFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-BroadworksDiameterFrontNodeFault
# Produced by pysmi-0.3.4 at Wed May  1 11:42:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
systemName, timeStamp, alarmName, alarmState, severity, identifier, recommendedActionsText, subcomponent, problemText, common, component, faultFields = mibBuilder.importSymbols("BroadworksFault", "systemName", "timeStamp", "alarmName", "alarmState", "severity", "identifier", "recommendedActionsText", "subcomponent", "problemText", "common", "component", "faultFields")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, MibIdentifier, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, TimeTicks, Integer32, ModuleIdentity, Counter64, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "MibIdentifier", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "TimeTicks", "Integer32", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2006-01-26 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: systemFaults.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200601260000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
if mibBuilder.loadTexts: systemFaults.setContactInfo('Broadsoft, Inc. 220 Perry Parkway Gaithersburg, MD 20877 301-977-9440')
if mibBuilder.loadTexts: systemFaults.setDescription('The defines the fault for the BroadWorks Diameter Server interconnect process.')
bwPMDiameterFrontNodeLaunched = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5101)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeLaunched.setStatus('current')
if mibBuilder.loadTexts: bwPMDiameterFrontNodeLaunched.setDescription('Indicates that the Diameter Front Node has been started. For a complete description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
bwPMDiameterFrontNodeShutDown = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5102)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeShutDown.setStatus('current')
if mibBuilder.loadTexts: bwPMDiameterFrontNodeShutDown.setDescription('Indicates that the Diameter Front Node has been manually shut down. For a complete description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
bwPMDiameterFrontNodeRestarted = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5103)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeRestarted.setStatus('current')
if mibBuilder.loadTexts: bwPMDiameterFrontNodeRestarted.setDescription('Indicates that the Diameter Front Node has been restarted. For a complete description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
bwPMDiameterFrontNodeDeath = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5104)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeDeath.setStatus('current')
if mibBuilder.loadTexts: bwPMDiameterFrontNodeDeath.setDescription('Indicates that the Diameter Front Node has terminated. For a complete description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
bwDiameterFrontNodeSyncFailure = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5105)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwDiameterFrontNodeSyncFailure.setStatus('current')
if mibBuilder.loadTexts: bwDiameterFrontNodeSyncFailure.setDescription('Indicates that the Execution Server encountered a failure messaging with the Diameter Front Node when synchronizing Diameter Front Node configuration data with the database. For a complete description, refer the BroadWorks FaultManagementGuide as it may contain variable data.')
mibBuilder.exportSymbols("BW-BroadworksDiameterFrontNodeFault", bwDiameterFrontNodeSyncFailure=bwDiameterFrontNodeSyncFailure, bwPMDiameterFrontNodeDeath=bwPMDiameterFrontNodeDeath, bwPMDiameterFrontNodeShutDown=bwPMDiameterFrontNodeShutDown, bwPMDiameterFrontNodeLaunched=bwPMDiameterFrontNodeLaunched, systemFaults=systemFaults, PYSNMP_MODULE_ID=systemFaults, bwPMDiameterFrontNodeRestarted=bwPMDiameterFrontNodeRestarted)
