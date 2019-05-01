#
# PySNMP MIB module TIMETRA-SAS-IEEE8021-CFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-SAS-IEEE8021-CFM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:21:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
dot1agCfmMepEntry, = mibBuilder.importSymbols("IEEE8021-CFM-MIB", "dot1agCfmMepEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Bits, Unsigned32, Counter32, Counter64, TimeTicks, Integer32, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Unsigned32", "Counter32", "Counter64", "TimeTicks", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Gauge32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
timetraSASConfs, timetraSASModules, timetraSASObjs = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASConfs", "timetraSASModules", "timetraSASObjs")
timetraSASIEEE8021CfmMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 11))
timetraSASIEEE8021CfmMIBModule.setRevisions(('1910-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setRevisionsDescriptions(('Rev 1.0 01 Jan 2010 00:00 Initial version of the TIMETRA-IEEE8021-CFM-MIB.',))
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setLastUpdated('0902280000Z')
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setOrganization('Alcatel')
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setContactInfo('Alcatel 7x50 Support Web: http://www.alcatel.com/comps/pages/carrier_support.jhtml')
if mibBuilder.loadTexts: timetraSASIEEE8021CfmMIBModule.setDescription("This document is the SNMP MIB module to manage and provision dot1ag Connectivity Fault Management module functionality for the Alcatel 7210 products. This includes extensions to the IEEE8021-CFM MIB. Copyright 2011-2013 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel's proprietary intellectual property. Alcatel retains all title and ownership in the Specification, including any revisions. Alcatel grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied 'as is', and Alcatel makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
tmnxSASDot1agMIBObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11))
tmnxSASDot1agMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7))
tmnxSASDot1agCfmMep = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1))
tmnxSASDot1agNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2))
tmnxSASDot1agNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 2, 1))
tmnxDot1agCfmMepExtnTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1), )
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnTable.setStatus('current')
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnTable.setDescription('This table augments the Maintenance Association End Point (MEP) table of the IEEE8021-CFM-MIB.')
tmnxDot1agCfmMepExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1), )
dot1agCfmMepEntry.registerAugmentions(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepExtnEntry"))
tmnxDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnEntry.setStatus('current')
if mibBuilder.loadTexts: tmnxDot1agCfmMepExtnEntry.setDescription('A conceptual row in the tmnxDot1agCfmMepExtnTable. This row exists only if the association dot1agCfmMepEntry is active.')
tmnxDot1agCfmMepSendAisOnPortDown = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxDot1agCfmMepSendAisOnPortDown.setStatus('current')
if mibBuilder.loadTexts: tmnxDot1agCfmMepSendAisOnPortDown.setDescription(' The value of tmnxDot1agCfmMepSendAisOnPortDown specifies that ETH-AIS should be generated for client MEP-s immediately when port down is detected on a SAP where server MEP resides')
tmnxDot1agCfmMepControlSapTag = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 11, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxDot1agCfmMepControlSapTag.setStatus('current')
if mibBuilder.loadTexts: tmnxDot1agCfmMepControlSapTag.setDescription(' tmnxDot1agCfmMepControlSapTag specifies the control sap tag.')
tmnxSASDot1agCfmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1))
tmnxSASDot1agCfmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2))
tmnxSASDot1agCfmComplianceV2v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 1, 2)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxSASDot1agCfmMepGroupV2v0"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmComplianceV2v0 = tmnxSASDot1agCfmComplianceV2v0.setStatus('current')
if mibBuilder.loadTexts: tmnxSASDot1agCfmComplianceV2v0.setDescription('The compliance statement for revision 2.0 of the 7210 system')
tmnxSASDot1agCfmMepGroupV2v0 = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 1)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmMepGroupV2v0 = tmnxSASDot1agCfmMepGroupV2v0.setStatus('current')
if mibBuilder.loadTexts: tmnxSASDot1agCfmMepGroupV2v0.setDescription('The group of objects for management of dot1ag MEP Table applicable to implementing SDP-Bindings.')
tmnxSASDot1agCfmMepGroupV4v0 = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 7, 2, 2)).setObjects(("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepSendAisOnPortDown"), ("TIMETRA-SAS-IEEE8021-CFM-MIB", "tmnxDot1agCfmMepControlSapTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxSASDot1agCfmMepGroupV4v0 = tmnxSASDot1agCfmMepGroupV4v0.setStatus('current')
if mibBuilder.loadTexts: tmnxSASDot1agCfmMepGroupV4v0.setDescription('The group of objects for management of dot1ag MEP Table applicable to implementing SDP-Bindings.')
mibBuilder.exportSymbols("TIMETRA-SAS-IEEE8021-CFM-MIB", tmnxSASDot1agCfmGroups=tmnxSASDot1agCfmGroups, tmnxSASDot1agNotifications=tmnxSASDot1agNotifications, tmnxSASDot1agCfmMepGroupV2v0=tmnxSASDot1agCfmMepGroupV2v0, tmnxSASDot1agMIBConformance=tmnxSASDot1agMIBConformance, tmnxDot1agCfmMepExtnTable=tmnxDot1agCfmMepExtnTable, tmnxDot1agCfmMepExtnEntry=tmnxDot1agCfmMepExtnEntry, tmnxSASDot1agNotificationsPrefix=tmnxSASDot1agNotificationsPrefix, PYSNMP_MODULE_ID=timetraSASIEEE8021CfmMIBModule, tmnxSASDot1agCfmComplianceV2v0=tmnxSASDot1agCfmComplianceV2v0, tmnxSASDot1agCfmMepGroupV4v0=tmnxSASDot1agCfmMepGroupV4v0, tmnxDot1agCfmMepSendAisOnPortDown=tmnxDot1agCfmMepSendAisOnPortDown, timetraSASIEEE8021CfmMIBModule=timetraSASIEEE8021CfmMIBModule, tmnxSASDot1agMIBObjs=tmnxSASDot1agMIBObjs, tmnxSASDot1agCfmCompliances=tmnxSASDot1agCfmCompliances, tmnxDot1agCfmMepControlSapTag=tmnxDot1agCfmMepControlSapTag, tmnxSASDot1agCfmMep=tmnxSASDot1agCfmMep)
