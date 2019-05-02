#
# PySNMP MIB module CAPWAP-DOT11-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CAPWAP-DOT11-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:46:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
CapwapBaseMacTypeTC, CapwapBaseTunnelModeTC = mibBuilder.importSymbols("CAPWAP-BASE-MIB", "CapwapBaseMacTypeTC", "CapwapBaseTunnelModeTC")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Counter64, Gauge32, TimeTicks, ObjectIdentity, iso, IpAddress, Integer32, ModuleIdentity, mib_2, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "TimeTicks", "ObjectIdentity", "iso", "IpAddress", "Integer32", "ModuleIdentity", "mib-2", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
capwapDot11MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 195))
capwapDot11MIB.setRevisions(('2010-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: capwapDot11MIB.setRevisionsDescriptions(('Initial version, published as RFC 5834',))
if mibBuilder.loadTexts: capwapDot11MIB.setLastUpdated('201004300000Z')
if mibBuilder.loadTexts: capwapDot11MIB.setOrganization('IETF Control And Provisioning of Wireless Access Points (CAPWAP) Working Group http://www.ietf.org/html.charters/capwap-charter.html')
if mibBuilder.loadTexts: capwapDot11MIB.setContactInfo('General Discussion: capwap@frascone.com To Subscribe: http://lists.frascone.com/mailman/listinfo/capwap Yang Shi (editor) Hangzhou H3C Tech. Co., Ltd. Beijing R&D Center of H3C, Digital Technology Plaza NO. 9 Shangdi 9th Street, Haidian District Beijing 100085 China Phone: +86 010 82775276 Email: rishyang@gmail.com David T. Perkins (editor) 228 Bayview Dr. San Carlos, CA 94070 USA Phone: +1 408 394-8702 Email: dperkins@dsperkins.com Chris Elliott (editor) 1516 Kent St. Durham, NC 27707 USA Phone: +1 919-308-1216 Email: chelliot@pobox.com Yong Zhang (editor) Fortinet, Inc. 1090 Kifer Road Sunnyvale, CA 94086 USA Email: yzhang@fortinet.com')
if mibBuilder.loadTexts: capwapDot11MIB.setDescription("Copyright (c) 2010 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This version of this MIB module is part of RFC 5834; see the RFC itself for full legal notices. This MIB module contains managed object definitions for CAPWAP Protocol binding for IEEE 802.11.")
class CapwapDot11WlanIdTC(TextualConvention, Unsigned32):
    description = 'Represents the unique identifier of a Wireless Local Area Network (WLAN).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16)

class CapwapDot11WlanIdProfileTC(TextualConvention, Unsigned32):
    description = 'Represents the unique identifier of a WLAN profile.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 512)

capwapDot11Objects = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 1))
capwapDot11Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 2))
capwapDot11WlanTable = MibTable((1, 3, 6, 1, 2, 1, 195, 1, 1), )
if mibBuilder.loadTexts: capwapDot11WlanTable.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanTable.setDescription('A table that allows the operator to display and configure WLAN profiles, such as specifying the MAC type and tunnel mode for a WLAN. Also, it helps the AC to configure a WLAN through the IEEE 802.11 MIB module. Values of all objects in this table are persistent at restart/reboot.')
capwapDot11WlanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 195, 1, 1, 1), ).setIndexNames((0, "CAPWAP-DOT11-MIB", "capwapDot11WlanProfileId"))
if mibBuilder.loadTexts: capwapDot11WlanEntry.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanEntry.setDescription('A set of objects that stores the settings of a WLAN profile.')
capwapDot11WlanProfileId = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 1), CapwapDot11WlanIdProfileTC())
if mibBuilder.loadTexts: capwapDot11WlanProfileId.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanProfileId.setDescription('Represents the identifier of a WLAN profile that has a corresponding capwapDot11WlanProfileIfIndex.')
capwapDot11WlanProfileIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapDot11WlanProfileIfIndex.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanProfileIfIndex.setDescription('Represents the index value that uniquely identifies a WLAN Profile Interface. The interface identified by a particular value of this index is the same interface as identified by the same value of the ifIndex. The creation of a row object in the capwapDot11WlanTable triggers the AC to automatically create an WLAN Profile Interface identified by an ifIndex without manual intervention. Most MIB tables in the IEEE 802.11 MIB module [IEEE.802-11.2007] use an ifIndex to identify an interface to facilitate the configuration and maintenance, for example, dot11AuthenticationAlgorithmsTable. Using the ifIndex of a WLAN Profile Interface, the Operator could configure a WLAN through the IEEE 802.11 MIB module.')
capwapDot11WlanMacType = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 3), CapwapBaseMacTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanMacType.setReference('Section 6.1 of CAPWAP Protocol Binding for IEEE 802.11, RFC 5416.')
if mibBuilder.loadTexts: capwapDot11WlanMacType.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanMacType.setDescription('Represents whether the WTP SHOULD support the WLAN in Local or Split MAC modes.')
capwapDot11WlanTunnelMode = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 4), CapwapBaseTunnelModeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanTunnelMode.setReference('Section 6.1 of CAPWAP Protocol Binding for IEEE 802.11, RFC 5416.')
if mibBuilder.loadTexts: capwapDot11WlanTunnelMode.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanTunnelMode.setDescription("Represents the frame tunneling mode to be used for IEEE 802.11 data frames from all stations associated with the WLAN. Bits are exclusive with each other for a specific WLAN profile, and only one tunnel mode could be configured. If the operator set more than one bit, the value of the Response-PDU's error-status field is set to 'wrongValue', and the value of its error-index field is set to the index of the failed variable binding.")
capwapDot11WlanRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanRowStatus.setDescription("This variable is used to create, modify, and/or delete a row in this table. All the objects in a row can be modified only when the value of this object in the corresponding conceptual row is not 'active'. Thus, to modify one or more of the objects in this conceptual row: a. change the row status to 'notInService', b. change the values of the row c. change the row status to 'active' The capwapDot11WlanRowStatus may be changed to 'active' if all the managed objects in the conceptual row with MAX-ACCESS read-create have been assigned valid values. When the operator deletes a WLAN profile, the AC SHOULD check whether the WLAN profile is bound with a radio. If yes, the value of the Response-PDU's error-status field is set to 'inconsistentValue', and the value of its error-index field is set to the index of the failed variable binding. If not, the row object could be deleted.")
capwapDot11WlanBindTable = MibTable((1, 3, 6, 1, 2, 1, 195, 1, 2), )
if mibBuilder.loadTexts: capwapDot11WlanBindTable.setReference('Section 6.1 of CAPWAP Protocol Binding for IEEE 802.11, RFC 5416.')
if mibBuilder.loadTexts: capwapDot11WlanBindTable.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanBindTable.setDescription('A table that stores bindings between WLAN profiles (identified by capwapDot11WlanProfileId) and WTP Virtual Radio Interfaces. The WTP Virtual Radio Interfaces on the AC correspond to physical layer (PHY) radios on the WTPs. It also stores the mappings between WLAN IDs and WLAN Basic Service Set (BSS) Interfaces. Values of all objects in this table are persistent at restart/reboot.')
capwapDot11WlanBindEntry = MibTableRow((1, 3, 6, 1, 2, 1, 195, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CAPWAP-DOT11-MIB", "capwapDot11WlanProfileId"))
if mibBuilder.loadTexts: capwapDot11WlanBindEntry.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanBindEntry.setDescription('A set of objects that stores the binding of a WLAN profile to a WTP Virtual Radio Interface. It also stores the mapping between WLAN ID and WLAN BSS Interface. The INDEX object ifIndex is the ifIndex of a WTP Virtual Radio Interface.')
capwapDot11WlanBindWlanId = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 1), CapwapDot11WlanIdTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapDot11WlanBindWlanId.setReference('Section 6.1 of CAPWAP Protocol Binding for IEEE 802.11, RFC 5416.')
if mibBuilder.loadTexts: capwapDot11WlanBindWlanId.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanBindWlanId.setDescription('Represents the WLAN ID of a WLAN. During a binding operation, the AC MUST select an unused WLAN ID from between 1 and 16 [RFC5416]. For example, to bind another WLAN profile to a radio that has been bound with a WLAN profile, WLAN ID 2 should be assigned.')
capwapDot11WlanBindBssIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapDot11WlanBindBssIfIndex.setReference('Section 2.4 of CAPWAP Protocol Binding for IEEE 802.11, RFC 5416.')
if mibBuilder.loadTexts: capwapDot11WlanBindBssIfIndex.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanBindBssIfIndex.setDescription('Represents the index value that uniquely identifies a WLAN BSS Interface. The interface identified by a particular value of this index is the same interface as identified by the same value of the ifIndex. The ifIndex here is for a WLAN BSS Interface. The creation of a row object in the capwapDot11WlanBindTable triggers the AC to automatically create a WLAN BSS Interface identified by an ifIndex without manual intervention. The PHY address of the capwapDot11WlanBindBssIfIndex is the BSSID. While manufacturers are free to assign BSSIDs by using any arbitrary mechanism, it is advised that where possible the BSSIDs are assigned as a contiguous block. When assigned as a block, implementations can still assign any of the available BSSIDs to any WLAN. One possible method is for the WTP to assign the address using the following algorithm: base BSSID address + WLAN ID.')
capwapDot11WlanBindRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 195, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: capwapDot11WlanBindRowStatus.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanBindRowStatus.setDescription("This variable is used to create, modify, and/or delete a row in this table. All the objects in a row can be modified only when the value of this object in the corresponding conceptual row is not 'active'. Thus, to modify one or more of the objects in this conceptual row: a. change the row status to 'notInService', b. change the values of the row c. change the row status to 'active'")
capwapDot11Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 2, 1))
capwapDot11Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 195, 2, 2))
capwapDot11Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 195, 2, 2, 1)).setObjects(("CAPWAP-DOT11-MIB", "capwapDot11WlanGroup"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capwapDot11Compliance = capwapDot11Compliance.setStatus('current')
if mibBuilder.loadTexts: capwapDot11Compliance.setDescription('Describes the requirements for conformance to the CAPWAP-DOT11-MIB module.')
capwapDot11WlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 195, 2, 1, 1)).setObjects(("CAPWAP-DOT11-MIB", "capwapDot11WlanProfileIfIndex"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanMacType"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanTunnelMode"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capwapDot11WlanGroup = capwapDot11WlanGroup.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanGroup.setDescription('A collection of objects that is used to configure the properties of a WLAN profile.')
capwapDot11WlanBindGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 195, 2, 1, 2)).setObjects(("CAPWAP-DOT11-MIB", "capwapDot11WlanBindWlanId"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindBssIfIndex"), ("CAPWAP-DOT11-MIB", "capwapDot11WlanBindRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capwapDot11WlanBindGroup = capwapDot11WlanBindGroup.setStatus('current')
if mibBuilder.loadTexts: capwapDot11WlanBindGroup.setDescription('A collection of objects that is used to bind the WLAN profiles with a radio.')
mibBuilder.exportSymbols("CAPWAP-DOT11-MIB", capwapDot11WlanBindEntry=capwapDot11WlanBindEntry, capwapDot11WlanBindGroup=capwapDot11WlanBindGroup, capwapDot11WlanBindRowStatus=capwapDot11WlanBindRowStatus, capwapDot11WlanTable=capwapDot11WlanTable, capwapDot11Conformance=capwapDot11Conformance, capwapDot11WlanMacType=capwapDot11WlanMacType, capwapDot11Groups=capwapDot11Groups, capwapDot11MIB=capwapDot11MIB, CapwapDot11WlanIdProfileTC=CapwapDot11WlanIdProfileTC, capwapDot11Compliances=capwapDot11Compliances, PYSNMP_MODULE_ID=capwapDot11MIB, capwapDot11Compliance=capwapDot11Compliance, capwapDot11WlanGroup=capwapDot11WlanGroup, capwapDot11WlanBindWlanId=capwapDot11WlanBindWlanId, CapwapDot11WlanIdTC=CapwapDot11WlanIdTC, capwapDot11WlanEntry=capwapDot11WlanEntry, capwapDot11WlanBindTable=capwapDot11WlanBindTable, capwapDot11WlanProfileIfIndex=capwapDot11WlanProfileIfIndex, capwapDot11Objects=capwapDot11Objects, capwapDot11WlanBindBssIfIndex=capwapDot11WlanBindBssIfIndex, capwapDot11WlanRowStatus=capwapDot11WlanRowStatus, capwapDot11WlanProfileId=capwapDot11WlanProfileId, capwapDot11WlanTunnelMode=capwapDot11WlanTunnelMode)
