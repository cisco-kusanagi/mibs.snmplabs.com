#
# PySNMP MIB module ALCATEL-IND1-VIRTUALROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-VIRTUALROUTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:18:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
routingIND1Vrf, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Vrf")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, Counter64, ModuleIdentity, Integer32, Counter32, ObjectIdentity, Gauge32, IpAddress, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "Gauge32", "IpAddress", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Bits")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
alcatelIND1VirtualRouterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1))
alcatelIND1VirtualRouterMIB.setRevisions(('2008-03-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setLastUpdated('201308230000Z')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1VirtualRouterMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): This proprietary MIB contains management information for the configuration of Virtual Router instances. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2006 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1VirtualRouterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1))
alaVirtualRouterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1))
alaVirtualRouterNameTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaVirtualRouterNameTable.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameTable.setDescription('Table containing Virtual Router Name to Virtual Router Index bindings. There is always an entry for the default Virtual Router which has the name default')
alaVirtualRouterNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterName"))
if mibBuilder.loadTexts: alaVirtualRouterNameEntry.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameEntry.setDescription('Each entry binds a Virtual Router Name to a Virtual Router index.')
alaVirtualRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20)))
if mibBuilder.loadTexts: alaVirtualRouterName.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterName.setDescription('The name of a Virtual Router.')
alaVirtualRouterNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterNameIndex.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameIndex.setDescription('The index associated with the Virtual Router name.')
alaVirtualRouterNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterNameRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNameRowStatus.setDescription('Controls creation and deletion of Row Status entries.')
alaVirtualRouterProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterProfile.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfile.setDescription('The profile name of the VRF. Profiles place constraints on what the VRF can contain.')
alaVirtualRouterMaxRouteMaps = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxRouteMaps.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterMaxRouteMaps.setDescription('The maximum number of route-maps allowed in this VRF.')
alaVirtualRouterMaxSequences = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxSequences.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterMaxSequences.setDescription('The maximum number of route-map sequences allowed in this VRF.')
alaVirtualRouterMaxTlvs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxTlvs.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterMaxTlvs.setDescription('The maximum number of route-map TLV blocks allowed in this VRF.')
alaVirtualRouterMaxAccessLists = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxAccessLists.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterMaxAccessLists.setDescription('The maximum number of access-lists allowed in this VRF.')
alaVirtualRouterMaxAddressBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxAddressBlocks.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterMaxAddressBlocks.setDescription('The maximum number of access-list address blocks allowed in this VRF.')
alaVirtualRouterMaxMatchInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVirtualRouterMaxMatchInterfaces.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterMaxMatchInterfaces.setDescription('The maximum number of route-map match interfaces allowed in this VRF.')
alaVirtualRouterNoAutoLoadVrrp = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVirtualRouterNoAutoLoadVrrp.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterNoAutoLoadVrrp.setDescription('If true, do not automatically load VRRP in max profile VRF.')
alaVrConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2), )
if mibBuilder.loadTexts: alaVrConfigTable.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigTable.setDescription('Table containing Virtual Router protocol configuration.')
alaVrConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigIndex"))
if mibBuilder.loadTexts: alaVrConfigEntry.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigEntry.setDescription('Each entry exists for each VRF in the alaVrtualRouterNameTable. The entry represents the status of routing protocols on a VRF instance.')
alaVrConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: alaVrConfigIndex.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigIndex.setDescription('The index associated with the Virtual Router name.')
alaVrConfigRipStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigRipStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigRipStatus.setDescription('Controls the load status of RIP on this router. Loaded(1) is the only valid Set value.')
alaVrConfigOspfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigOspfStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigOspfStatus.setDescription('Controls the load status of OSPF on this router. Loaded(1) is the only valid Set value.')
alaVrConfigIsisStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigIsisStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigIsisStatus.setDescription('Controls the load status of ISIS on this router. Loaded(1) is the only valid Set value.')
alaVrConfigBgpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigBgpStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigBgpStatus.setDescription('Controls the load status of BGP on this router. Loaded(1) is the only valid Set value.')
alaVrConfigPimStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigPimStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigPimStatus.setDescription('Controls the load status of PIM on this router. Loaded(1) is the only valid Set value.')
alaVrConfigDvmrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigDvmrpStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigDvmrpStatus.setDescription('Controls the load status of DVMRP on this router. Loaded(1) is the only valid Set value.')
alaVrConfigRipngStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigRipngStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigRipngStatus.setDescription('Controls the load status of Ripng on this router. Loaded(1) is the only valid Set value.')
alaVrConfigOspf3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigOspf3Status.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigOspf3Status.setDescription('Controls the load status of OSPFv3 on this router. Loaded(1) is the only valid Set value.')
alaVrConfigMplsLdpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrConfigMplsLdpStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigMplsLdpStatus.setDescription('Controls the load status of MPLS LDP on this router. Loaded(1) is the only valid Set value.')
alaVrConfigVrrpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loaded", 1), ("notloaded", 2), ("loading", 3))).clone('notloaded')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrConfigVrrpStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrConfigVrrpStatus.setDescription('Controls the load status of VRRP on this router. Loaded(1) is the only valid Set value.')
alaVirtualRouterProfileTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3), )
if mibBuilder.loadTexts: alaVirtualRouterProfileTable.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileTable.setDescription('Table contains capabilities of a VRF profile.')
alaVirtualRouterProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileName"))
if mibBuilder.loadTexts: alaVirtualRouterProfileEntry.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileEntry.setDescription('Each entry defines a VRF profile.')
alaVirtualRouterProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: alaVirtualRouterProfileName.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileName.setDescription('The name of the profile.')
alaVirtualRouterProfileMaxRouteMaps = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxRouteMaps.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxRouteMaps.setDescription('The maximum number of route-maps supported in this VRF profile.')
alaVirtualRouterProfileMaxSequences = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxSequences.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxSequences.setDescription('The maximum number of route-map sequences supported in this VRF profile.')
alaVirtualRouterProfileMaxTlvs = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxTlvs.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxTlvs.setDescription('The maximum number of route-map TLVs supported in this VRF profile. TLVs are used to store match and set clauses.')
alaVirtualRouterProfileMaxAccessLists = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxAccessLists.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxAccessLists.setDescription('The maximum number of route-map access-lists supported in this VRF profile. Access-lists contain IPv4 or IPv6 addresses.')
alaVirtualRouterProfileMaxAddressBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxAddressBlocks.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxAddressBlocks.setDescription('The maximum number of route-map address blocks supported in this VRF profile. Address blocks are used to hold the access-lists routes.')
alaVirtualRouterProfileMaxMatchInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 1, 1, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxMatchInterfaces.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterProfileMaxMatchInterfaces.setDescription('The maximum number of route-map interfaces that can be configured match clauses supported in this VRF profile.')
alcatelIND1VirtualRouterMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2))
alcatelIND1VirtualRouterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 1))
alcatelIND1VirtualRouterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 2))
alaVirtualRouterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterCompliance = alaVirtualRouterCompliance.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterCompliance.setDescription('The compliance statement for routers running Route Maps and implementing the ALCATEL-IND1-VIRTUALROUTER MIB.')
alaVirtualRouterConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 15, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameIndex"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNameRowStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfile"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxRouteMaps"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxSequences"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxTlvs"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxAccessLists"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxAddressBlocks"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterMaxMatchInterfaces"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterNoAutoLoadVrrp"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigRipStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigOspfStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigIsisStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigBgpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigPimStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigDvmrpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigRipngStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigOspf3Status"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigMplsLdpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVrConfigVrrpStatus"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxRouteMaps"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxSequences"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxTlvs"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxAccessLists"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxAddressBlocks"), ("ALCATEL-IND1-VIRTUALROUTER-MIB", "alaVirtualRouterProfileMaxMatchInterfaces"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVirtualRouterConfigMIBGroup = alaVirtualRouterConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaVirtualRouterConfigMIBGroup.setDescription('A collection of objects to support management of global configuration parameters of the Virtual Router Module.')
mibBuilder.exportSymbols("ALCATEL-IND1-VIRTUALROUTER-MIB", alaVrConfigBgpStatus=alaVrConfigBgpStatus, alaVrConfigPimStatus=alaVrConfigPimStatus, alaVirtualRouterProfileName=alaVirtualRouterProfileName, alaVirtualRouterCompliance=alaVirtualRouterCompliance, alaVrConfigRipStatus=alaVrConfigRipStatus, alcatelIND1VirtualRouterMIBCompliances=alcatelIND1VirtualRouterMIBCompliances, alaVirtualRouterMaxRouteMaps=alaVirtualRouterMaxRouteMaps, alaVirtualRouterMaxSequences=alaVirtualRouterMaxSequences, alaVirtualRouterProfileMaxTlvs=alaVirtualRouterProfileMaxTlvs, alaVrConfigTable=alaVrConfigTable, alaVirtualRouterProfileMaxSequences=alaVirtualRouterProfileMaxSequences, alaVirtualRouterConfigMIBGroup=alaVirtualRouterConfigMIBGroup, alaVirtualRouterNameRowStatus=alaVirtualRouterNameRowStatus, alaVirtualRouterMaxTlvs=alaVirtualRouterMaxTlvs, alaVirtualRouterConfig=alaVirtualRouterConfig, alaVrConfigVrrpStatus=alaVrConfigVrrpStatus, alaVirtualRouterProfileMaxAccessLists=alaVirtualRouterProfileMaxAccessLists, alaVirtualRouterNameIndex=alaVirtualRouterNameIndex, alaVirtualRouterNameTable=alaVirtualRouterNameTable, alaVirtualRouterProfileMaxMatchInterfaces=alaVirtualRouterProfileMaxMatchInterfaces, alaVirtualRouterMaxAddressBlocks=alaVirtualRouterMaxAddressBlocks, alcatelIND1VirtualRouterMIB=alcatelIND1VirtualRouterMIB, alaVrConfigIndex=alaVrConfigIndex, alaVrConfigRipngStatus=alaVrConfigRipngStatus, alaVrConfigOspf3Status=alaVrConfigOspf3Status, alaVrConfigEntry=alaVrConfigEntry, alaVirtualRouterProfileEntry=alaVirtualRouterProfileEntry, alaVirtualRouterNameEntry=alaVirtualRouterNameEntry, alaVirtualRouterProfileMaxRouteMaps=alaVirtualRouterProfileMaxRouteMaps, alaVirtualRouterNoAutoLoadVrrp=alaVirtualRouterNoAutoLoadVrrp, alaVirtualRouterMaxMatchInterfaces=alaVirtualRouterMaxMatchInterfaces, alaVrConfigDvmrpStatus=alaVrConfigDvmrpStatus, alaVirtualRouterProfileMaxAddressBlocks=alaVirtualRouterProfileMaxAddressBlocks, alaVirtualRouterProfileTable=alaVirtualRouterProfileTable, alcatelIND1VirtualRouterMIBConformance=alcatelIND1VirtualRouterMIBConformance, alaVrConfigOspfStatus=alaVrConfigOspfStatus, alcatelIND1VirtualRouterMIBObjects=alcatelIND1VirtualRouterMIBObjects, PYSNMP_MODULE_ID=alcatelIND1VirtualRouterMIB, alaVrConfigIsisStatus=alaVrConfigIsisStatus, alaVrConfigMplsLdpStatus=alaVrConfigMplsLdpStatus, alaVirtualRouterName=alaVirtualRouterName, alcatelIND1VirtualRouterMIBGroups=alcatelIND1VirtualRouterMIBGroups, alaVirtualRouterMaxAccessLists=alaVirtualRouterMaxAccessLists, alaVirtualRouterProfile=alaVirtualRouterProfile)