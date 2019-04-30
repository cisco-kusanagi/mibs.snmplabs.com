#
# PySNMP MIB module BW-BroadworksDiameterFrontNodeFault (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-BroadworksDiameterFrontNodeFault
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
problemText, recommendedActionsText, severity, systemName, common, alarmName, timeStamp, subcomponent, faultFields, alarmState, component, identifier = mibBuilder.importSymbols("BroadworksFault", "problemText", "recommendedActionsText", "severity", "systemName", "common", "alarmName", "timeStamp", "subcomponent", "faultFields", "alarmState", "component", "identifier")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, NotificationType, Gauge32, TimeTicks, IpAddress, Counter32, ModuleIdentity, iso, Integer32, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "NotificationType", "Gauge32", "TimeTicks", "IpAddress", "Counter32", "ModuleIdentity", "iso", "Integer32", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
systemFaults = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1))
systemFaults.setRevisions(('2006-01-26 00:01',))
if mibBuilder.loadTexts: systemFaults.setLastUpdated('200601260000Z')
if mibBuilder.loadTexts: systemFaults.setOrganization('Broadsoft, Inc')
bwPMDiameterFrontNodeLaunched = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5101)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeLaunched.setStatus('current')
bwPMDiameterFrontNodeShutDown = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5102)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeShutDown.setStatus('current')
bwPMDiameterFrontNodeRestarted = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5103)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeRestarted.setStatus('current')
bwPMDiameterFrontNodeDeath = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5104)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwPMDiameterFrontNodeDeath.setStatus('current')
bwDiameterFrontNodeSyncFailure = NotificationType((1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5105)).setObjects(("BroadworksFault", "identifier"), ("BroadworksFault", "timeStamp"), ("BroadworksFault", "alarmName"), ("BroadworksFault", "systemName"), ("BroadworksFault", "severity"), ("BroadworksFault", "component"), ("BroadworksFault", "subcomponent"), ("BroadworksFault", "problemText"), ("BroadworksFault", "recommendedActionsText"))
if mibBuilder.loadTexts: bwDiameterFrontNodeSyncFailure.setStatus('current')
mibBuilder.exportSymbols("BW-BroadworksDiameterFrontNodeFault", bwPMDiameterFrontNodeShutDown=bwPMDiameterFrontNodeShutDown, bwPMDiameterFrontNodeRestarted=bwPMDiameterFrontNodeRestarted, bwDiameterFrontNodeSyncFailure=bwDiameterFrontNodeSyncFailure, systemFaults=systemFaults, PYSNMP_MODULE_ID=systemFaults, bwPMDiameterFrontNodeLaunched=bwPMDiameterFrontNodeLaunched, bwPMDiameterFrontNodeDeath=bwPMDiameterFrontNodeDeath)
