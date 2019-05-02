#
# PySNMP MIB module TIMETRA-SAS-IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:21:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
dot1xAuthConfigEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthConfigEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, NotificationType, Gauge32, MibIdentifier, ModuleIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, Counter64, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "ModuleIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "Counter64", "IpAddress", "Unsigned32")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
timetraSASNotifyPrefix, timetraSASConfs, timetraSASModules, timetraSASObjs = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASNotifyPrefix", "timetraSASConfs", "timetraSASModules", "timetraSASObjs")
TNamedItem, TPolicyStatementNameOrEmpty, ServiceAdminStatus = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TNamedItem", "TPolicyStatementNameOrEmpty", "ServiceAdminStatus")
timeraSASIEEE8021PaeMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 17))
timeraSASIEEE8021PaeMIBModule.setRevisions(('1912-07-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setRevisionsDescriptions(('Rev 1.0 03 Aug 2012 00:00 1.0 release of the ALCATEL-SAS-IEEE8021-PAE-MIB.',))
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setLastUpdated('1207010000Z')
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setContactInfo('Alcatel-Lucent SROS Support Web: http://support.alcatel-lucent.com ')
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setDescription("This document is the SNMP MIB module to manage and provision the 7x50 extensions to the IEEE8021-PAE-MIB (Port Access Entity nodule for managing IEEE 802.X) feature for the Alcatel 7210 device. Copyright 2004-2012 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel-Lucent's proprietary intellectual property. Alcatel-Lucent retains all title and ownership in the Specification, including any revisions. Alcatel-Lucent grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel-Lucent products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied 'as is', and Alcatel-Lucent makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
tmnxSASDot1xObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16))
tmnxSASDot1xAuthenticatorObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1))
tmnxSASDot1xConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12))
tmnxDot1xSASCompliancs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1))
tmnxDot1xSASGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2))
dot1xAuthConfigExtnTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1), )
if mibBuilder.loadTexts: dot1xAuthConfigExtnTable.setStatus('current')
if mibBuilder.loadTexts: dot1xAuthConfigExtnTable.setDescription('The table dot1xAuthConfigExtnTable allows configuration of RADIUS authentication parameters for the 802.1X PAE feature on port level.')
dot1xAuthConfigExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1), )
dot1xAuthConfigEntry.registerAugmentions(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xAuthConfigExtnEntry"))
dot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
if mibBuilder.loadTexts: dot1xAuthConfigExtnEntry.setStatus('current')
if mibBuilder.loadTexts: dot1xAuthConfigExtnEntry.setDescription('dot1xAuthConfigExtnEntry is an entry (conceptual row) in the dot1xAuthConfigExtnTable. Each entry represents the configuration for Radius Authentication on a port. Entries have a presumed StorageType of nonVolatile.')
dot1xPortEtherTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1, 150), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPortEtherTunnel.setStatus('current')
if mibBuilder.loadTexts: dot1xPortEtherTunnel.setDescription('The value of tmnxPortEtherDot1xTunnel specifies whether the DOT1X packet tunneling for the ethernet port is enabled or disabled. When tunneling is enabled, the port will not process any DOT1X packets but will tunnel them through instead.')
dot1xAuthConfigExtnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2, 1)).setObjects(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xPortEtherTunnel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xAuthConfigExtnGroup = dot1xAuthConfigExtnGroup.setStatus('current')
if mibBuilder.loadTexts: dot1xAuthConfigExtnGroup.setDescription('The group of objects supporting management of Radius authentication for the IEEE801.1X PAE feature on Alcatel 7210 SR series systems.')
dot1xAuthConfigExtnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1, 1)).setObjects(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xAuthConfigExtnGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xAuthConfigExtnCompliance = dot1xAuthConfigExtnCompliance.setStatus('current')
if mibBuilder.loadTexts: dot1xAuthConfigExtnCompliance.setDescription('The compliance statement for management of Radius authentication for the IEEE801.1X PAE feature on Alcatel 7210 SR series systems.')
mibBuilder.exportSymbols("TIMETRA-SAS-IEEE8021-PAE-MIB", dot1xAuthConfigExtnGroup=dot1xAuthConfigExtnGroup, dot1xAuthConfigExtnEntry=dot1xAuthConfigExtnEntry, tmnxSASDot1xObjs=tmnxSASDot1xObjs, timeraSASIEEE8021PaeMIBModule=timeraSASIEEE8021PaeMIBModule, tmnxDot1xSASGroups=tmnxDot1xSASGroups, PYSNMP_MODULE_ID=timeraSASIEEE8021PaeMIBModule, dot1xAuthConfigExtnCompliance=dot1xAuthConfigExtnCompliance, tmnxDot1xSASCompliancs=tmnxDot1xSASCompliancs, dot1xPortEtherTunnel=dot1xPortEtherTunnel, tmnxSASDot1xConformance=tmnxSASDot1xConformance, dot1xAuthConfigExtnTable=dot1xAuthConfigExtnTable, tmnxSASDot1xAuthenticatorObjs=tmnxSASDot1xAuthenticatorObjs)
