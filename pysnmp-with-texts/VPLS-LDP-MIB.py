#
# PySNMP MIB module VPLS-LDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPLS-LDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
pwIndex, pwID = mibBuilder.importSymbols("PW-STD-MIB", "pwIndex", "pwID")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, NotificationType, Bits, IpAddress, Counter32, TimeTicks, MibIdentifier, ObjectIdentity, transmission, Unsigned32, iso, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "NotificationType", "Bits", "IpAddress", "Counter32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "transmission", "Unsigned32", "iso", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
vplsConfigIndex, vplsConfigName = mibBuilder.importSymbols("VPLS-GENERIC-MIB", "vplsConfigIndex", "vplsConfigName")
vplsLdpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 275))
vplsLdpMIB.setRevisions(('2014-05-19 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vplsLdpMIB.setRevisionsDescriptions(('Initial version published as part of RFC 7257.',))
if mibBuilder.loadTexts: vplsLdpMIB.setLastUpdated('201405191200Z')
if mibBuilder.loadTexts: vplsLdpMIB.setOrganization('Layer 2 Virtual Private Networks (L2VPN) Working Group')
if mibBuilder.loadTexts: vplsLdpMIB.setContactInfo(' Rohit Mediratta Email: romedira@cisco.com The L2VPN Working Group (email distribution l2vpn@ietf.org, http://www.ietf.org/wg/l2vpn/charter/) ')
if mibBuilder.loadTexts: vplsLdpMIB.setDescription("Copyright (c) 2014 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). The initial version of this MIB module was published in RFC 7257; for full legal notices see the RFC itself. This MIB module contains managed object definitions for LDP-signaled Virtual Private LAN Services as in RFC 4762. This MIB module enables the use of any underlying pseudowire network.")
vplsLdpNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 0))
vplsLdpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 1))
vplsLdpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2))
vplsLdpConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 275, 1, 1), )
if mibBuilder.loadTexts: vplsLdpConfigTable.setStatus('current')
if mibBuilder.loadTexts: vplsLdpConfigTable.setDescription('This table specifies information for configuring and monitoring LDP-specific parameters for Virtual Private LAN Service (VPLS).')
vplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"))
if mibBuilder.loadTexts: vplsLdpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: vplsLdpConfigEntry.setDescription('A row in this table represents LDP-specific information for Virtual Private LAN Service (VPLS) in a packet network. It is indexed by vplsConfigIndex, which uniquely identifies a single VPLS. A row is automatically created when a VPLS service is configured using LDP signaling. All of the writable objects values can be changed when vplsConfigRowStatus is in the active(1) state. ')
vplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 275, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsLdpConfigMacAddrWithdraw.setStatus('current')
if mibBuilder.loadTexts: vplsLdpConfigMacAddrWithdraw.setDescription("This object specifies if MAC address withdrawal is enabled in this service. If this object is 'true', then MAC address withdrawal is enabled. If 'false', then MAC address withdrawal is disabled.")
vplsLdpPwBindTable = MibTable((1, 3, 6, 1, 2, 1, 10, 275, 1, 2), )
if mibBuilder.loadTexts: vplsLdpPwBindTable.setStatus('current')
if mibBuilder.loadTexts: vplsLdpPwBindTable.setDescription('This table provides LDP-specific information for an association between a VPLS service and the corresponding pseudowires. A service can have more than one pseudowire association. Pseudowires are defined in the pwTable.')
vplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1), ).setIndexNames((0, "VPLS-GENERIC-MIB", "vplsConfigIndex"), (0, "PW-STD-MIB", "pwIndex"))
if mibBuilder.loadTexts: vplsLdpPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: vplsLdpPwBindEntry.setDescription('Each row represents an association between a VPLS instance and one or more pseudowires defined in the pwTable. Each index is unique in describing an entry in this table. However, both indexes are required to define the one-to-many association of service to pseudowire. An entry in this table in instantiated only when LDP signaling is used to configure VPLS service. Each entry in this table provides LDP-specific information for the VPLS represented by vplsConfigIndex.')
vplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 275, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vplsLdpPwBindMacAddressLimit.setStatus('current')
if mibBuilder.loadTexts: vplsLdpPwBindMacAddressLimit.setDescription('The value of this object specifies the maximum number of learned and static entries allowed in the Forwarding database for this PW Binding. The value 0 means there is no limit for this PW Binding.')
vplsLdpPwBindMacTableFull = NotificationType((1, 3, 6, 1, 2, 1, 10, 275, 0, 1)).setObjects(("VPLS-GENERIC-MIB", "vplsConfigName"), ("PW-STD-MIB", "pwID"))
if mibBuilder.loadTexts: vplsLdpPwBindMacTableFull.setStatus('current')
if mibBuilder.loadTexts: vplsLdpPwBindMacTableFull.setDescription('The vplsLdpPwBindMacTableFull notification is generated when the number of learned MAC addresses increases to the value specified in vplsLdpPwBindMacAddressLimit.')
vplsLdpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2, 1))
vplsLdpModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 1)).setObjects(("VPLS-LDP-MIB", "vplsLdpGroup"), ("VPLS-LDP-MIB", "vplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpModuleFullCompliance = vplsLdpModuleFullCompliance.setStatus('current')
if mibBuilder.loadTexts: vplsLdpModuleFullCompliance.setDescription('Compliance requirement for implementations that provide full support for VPLS-LDP-MIB. Such devices can then be monitored and configured using this MIB module.')
vplsLdpModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 275, 2, 1, 2)).setObjects(("VPLS-LDP-MIB", "vplsLdpGroup"), ("VPLS-LDP-MIB", "vplsLdpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpModuleReadOnlyCompliance = vplsLdpModuleReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: vplsLdpModuleReadOnlyCompliance.setDescription('Compliance requirement for implementations that only provide read-only support for VPLS-LDP-MIB. Such devices can then be monitored but cannot be configured using this MIB modules.')
vplsLdpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 275, 2, 2))
vplsLdpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 1)).setObjects(("VPLS-LDP-MIB", "vplsLdpConfigMacAddrWithdraw"), ("VPLS-LDP-MIB", "vplsLdpPwBindMacAddressLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpGroup = vplsLdpGroup.setStatus('current')
if mibBuilder.loadTexts: vplsLdpGroup.setDescription('The group of objects supporting management of L2VPN VPLS services using LDP.')
vplsLdpNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 275, 2, 2, 2)).setObjects(("VPLS-LDP-MIB", "vplsLdpPwBindMacTableFull"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vplsLdpNotificationGroup = vplsLdpNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vplsLdpNotificationGroup.setDescription('The group of notifications supporting the Notifications generated for VPLS LDP Service.')
mibBuilder.exportSymbols("VPLS-LDP-MIB", vplsLdpPwBindEntry=vplsLdpPwBindEntry, vplsLdpGroups=vplsLdpGroups, vplsLdpGroup=vplsLdpGroup, PYSNMP_MODULE_ID=vplsLdpMIB, vplsLdpObjects=vplsLdpObjects, vplsLdpConformance=vplsLdpConformance, vplsLdpNotificationGroup=vplsLdpNotificationGroup, vplsLdpConfigEntry=vplsLdpConfigEntry, vplsLdpCompliances=vplsLdpCompliances, vplsLdpPwBindMacAddressLimit=vplsLdpPwBindMacAddressLimit, vplsLdpPwBindMacTableFull=vplsLdpPwBindMacTableFull, vplsLdpModuleFullCompliance=vplsLdpModuleFullCompliance, vplsLdpConfigTable=vplsLdpConfigTable, vplsLdpModuleReadOnlyCompliance=vplsLdpModuleReadOnlyCompliance, vplsLdpMIB=vplsLdpMIB, vplsLdpPwBindTable=vplsLdpPwBindTable, vplsLdpConfigMacAddrWithdraw=vplsLdpConfigMacAddrWithdraw, vplsLdpNotifications=vplsLdpNotifications)
