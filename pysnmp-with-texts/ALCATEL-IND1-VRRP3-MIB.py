#
# PySNMP MIB module ALCATEL-IND1-VRRP3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-VRRP3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:20:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1Vrrp, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Vrrp")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter64, Gauge32, Unsigned32, Bits, Integer32, ModuleIdentity, iso, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter64", "Gauge32", "Unsigned32", "Bits", "Integer32", "ModuleIdentity", "iso", "IpAddress", "ObjectIdentity")
RowStatus, TimeStamp, MacAddress, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "MacAddress", "TruthValue", "DisplayString", "TextualConvention")
VrId, = mibBuilder.importSymbols("VRRP-MIB", "VrId")
alcatelIND1VRRP3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2))
alcatelIND1VRRP3MIB.setRevisions(('2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1VRRP3MIB.setRevisionsDescriptions(('The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1VRRP3MIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1VRRP3MIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1VRRP3MIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1VRRP3MIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): Proprietary VRRP MIB definitions for simultaneous support of IPv4 and IPv6 protocols. The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alaVrrp3Operations = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1))
alaVrrp3Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2))
alaVrrp3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3))
alaVrrp3NotificationCntl = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaVrrp3NotificationCntl.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3NotificationCntl.setDescription("Indicates whether the VRRP-enabled router will generate SNMP traps for events defined in this MIB. 'Enabled' results in SNMP traps; 'disabled', no traps are sent.")
alaVrrp3OperTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2), )
if mibBuilder.loadTexts: alaVrrp3OperTable.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperTable.setDescription("Unified Operations table for a VRRP router which consists of a sequence (i.e., one or more conceptual rows) of 'alaVrrp3OperEntry' items.")
alaVrrp3OperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpVersion"), (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVrId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: alaVrrp3OperEntry.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperEntry.setDescription("An entry in the alaVrrp3OperTable containing the operational characteristics of a virtual router. On a VRRP router, a given virtual router is identified by a combination of the IP version, VRID, and ifIndex. Note that rows in this table can be distinguished on a Multi-stacked device running both VRRP over IPv4 and IPv6 interfaces. Rows in the table cannot be modified unless the value of 'alaVrrp3OperAdminState' is 'disabled' and the 'alaVrrp3OperState' has transitioned to 'initialize'")
alaVrrp3OperIpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: alaVrrp3OperIpVersion.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperIpVersion.setDescription('This object contains the IP version on which this VRRP instance is running.')
alaVrrp3OperVrId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 2), VrId())
if mibBuilder.loadTexts: alaVrrp3OperVrId.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperVrId.setDescription('This object contains the Virtual Router Identifier (VRID).')
alaVrrp3OperVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperVirtualMacAddr.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperVirtualMacAddr.setDescription("The virtual MAC address of the virtual router. Although this object can be derived from the 'alaVrrp3OperVrId' object, it is defined so that it is easily obtainable by a management application and can be included in VRRP-related SNMP traps.")
alaVrrp3OperState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperState.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperState.setDescription("The current state of the virtual router. This object has three defined values: - `initialize', which indicates that the virtual router is waiting for a startup event. - `backup', which indicates the virtual router is monitoring the availability of the master router. - `master', which indicates that the virtual router is forwarding packets for IP addresses that are associated with this router. Setting the `alaVrrp3OperAdminState' object (below) Initiates transitions in the value of this object.")
alaVrrp3OperAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVrrp3OperAdminState.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperAdminState.setDescription("This object will enable/disable the virtual router function. Setting the value to `up', will transition the state of the virtual router from `initialize' to `backup' or `master', depending on the value of `alaVrrp3OperPriority'. Setting the value to `down', will transition the router from `master' or `backup' to `initialize'. State transitions may not be immediate; they sometimes depend on other factors, such as the interface (IF) state. The `alaVrrp3OperAdminState' object must be set to `down' prior to modifying the other read-create objects in the conceptual row. The value of the alaVrrp3OperRowStatus' object (below) must be `active', signifying that the conceptual row is valid (i.e., the objects are correctly set), in order for this object to be set to `up'.")
alaVrrp3OperPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVrrp3OperPriority.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperPriority.setDescription("This object specifies the priority to be used for the virtual router master election process. Higher values imply higher priority. A priority of '0', although not settable, is sent by the master router to indicate that this router has ceased to participate in VRRP and a backup virtual router should transition to become a new master. A priority of 255 is used for the router that owns the associated IP address(es).")
alaVrrp3OperVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vrrpv2", 1), ("vrrpv3", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperVersion.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperVersion.setDescription('This object contains the VRRP version this VRRP instance is running.')
alaVrrp3OperIpAddrCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperIpAddrCount.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperIpAddrCount.setDescription('The number of IP addresses associated with this virtual router. This number is equal to the number of rows in the alaVrrp3AssoIpAddrTable that correspond to a given combination of IP version, VRID, and ifIndex.')
alaVrrp3OperMasterIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 9), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperMasterIpAddrType.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperMasterIpAddrType.setDescription('This specifies the type of alaVrrp3OperMasterIpAddr in this row.')
alaVrrp3OperMasterIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 10), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperMasterIpAddr.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperMasterIpAddr.setDescription("The master router's real (primary for vrrp over IPv4) IP address. This is the IP address listed as the source in the advertisement last received by this virtual router. For IPv6, a link local address.")
alaVrrp3OperPrimaryIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 11), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperPrimaryIpAddrType.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperPrimaryIpAddrType.setDescription('This specifies the the type of alaVrrp3OperPrimaryIpAddr in this row.')
alaVrrp3OperPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 12), InetAddress().clone(hexValue="00000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperPrimaryIpAddr.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperPrimaryIpAddr.setDescription("For VRRP over IPv6 this is the link local address for a given ifIndex. For VRRP over IPv4, in the case where there is more than one IP address for a given `ifIndex', this object is used to specify the IP address that will become the alaVrrp3OperMasterIpAddr', should the virtual router transition from backup to master.")
alaVrrp3OperAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(100)).setUnits('centiseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVrrp3OperAdvInterval.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperAdvInterval.setDescription('The time interval, in centiseconds, between sending advertisement messages. Only the master router sends VRRP advertisements.')
alaVrrp3OperPreemptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 14), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVrrp3OperPreemptMode.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperPreemptMode.setDescription('Controls whether a higher priority virtual router will preempt a lower priority master.')
alaVrrp3OperAcceptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 15), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVrrp3OperAcceptMode.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperAcceptMode.setDescription("Controls whether a virtual router in the master state will accept packets addressed to the address owner's IPv6 address as its own it it is not the IP address owner. This is required only for rows indicating VRRP over IPv6. This object can be sparse and should not be implemented for rows indicating VRRP for Ipv4.")
alaVrrp3OperUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 16), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3OperUpTime.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperUpTime.setDescription("This is the value of the `sysUpTime' object when this virtual router (i.e., the `alaVrrp3OperState') transitioned out of `initialized'.")
alaVrrp3OperRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 2, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVrrp3OperRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperRowStatus.setDescription("The row status variable, used in accordance to installation and removal conventions for conceptual rows. The rowstatus of a currently active row in the alaVrrp3OperTable is constrained by the operational state of the corresponding virtual router. When `alaVrrp3OperRowStatus' is set to active(1), no other objects in the conceptual row, with the exception of `alaVrrp3OperAdminState', can be modified. Prior to setting the `alaVrrp3OperRowStatus' object from `active' to a different value, the `alaVrrp3OperAdminState' object must be set to `down' and the `alaVrrp3OperState' object be transitioned to `initialize'. To create a row in this table, a manager sets this object to either createAndGo(4) or createAndWait(5). Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the `alaVrrp3OperRowStatus' column will be read as notReady(3). In particular, a newly created row cannot be made active(1) until (minimally) the corresponding instance of `alaVrrp3OperVrId' has been set and there is at least one active row in the `alaVrrp3AssoIpAddrTable' defining an associated IP address for the virtual router.")
alaVrrp3AssoIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3), )
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrTable.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrTable.setDescription('The table of addresses associated with this virtual router.')
alaVrrp3AssoIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpVersion"), (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVrId"), (0, "IF-MIB", "ifIndex"), (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3AssoIpAddrType"), (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3AssoIpAddr"))
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrEntry.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrEntry.setDescription("An entry in the table contains an IP address that is associated with a virtual router. The number of rows for a given IP version, VrId, and ifIndex will equal the number of IP addresses associated (e.g., backed up) by the virtual router (equivalent to 'alaVrrp3OperIpAddrCount'). Rows in the table cannot be modified unless the value of `alaVrrp3OperAdminState' is `disabled' and the `alaVrrp3OperState' has transitioned to`initialize'.")
alaVrrp3AssoIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrType.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrType.setDescription('The IP addresses type of alaVrrp3AssoIpAddr in this row.')
alaVrrp3AssoIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: alaVrrp3AssoIpAddr.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3AssoIpAddr.setDescription('The assigned IP addresses that a virtual router is responsible for backing up.')
alaVrrp3AssoIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3AssoIpAddrRowStatus.setDescription('The row status variable, used according to installation and removal conventions for conceptual rows. Setting this object to active(1) or createAndGo(4) results in the addition of an associated address for a virtual router. Destroying the entry or setting it to notInService(2) removes the associated address from the virtual router. The use of other values is implementation-dependent.')
alaVrrp3RouterChecksumErrors = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3RouterChecksumErrors.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3RouterChecksumErrors.setDescription('The total number of VRRP packets received with an invalid VRRP checksum value.')
alaVrrp3RouterVersionErrors = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3RouterVersionErrors.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3RouterVersionErrors.setDescription('The total number of VRRP packets received with an unknown or unsupported version number.')
alaVrrp3RouterVrIdErrors = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3RouterVrIdErrors.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3RouterVrIdErrors.setDescription('The total number of VRRP packets received with an invalid VRID for this virtual router.')
alaVrrp3RouterStatsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4), )
if mibBuilder.loadTexts: alaVrrp3RouterStatsTable.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3RouterStatsTable.setDescription('Table of virtual router statistics.')
alaVrrp3RouterStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1), ).setIndexNames((0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpVersion"), (0, "ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVrId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: alaVrrp3RouterStatsEntry.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3RouterStatsEntry.setDescription('An entry in the table, containing statistics information about a given virtual router.')
alaVrrp3StatsBecomeMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsBecomeMaster.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsBecomeMaster.setDescription("The total number of times that this virtual router's state has transitioned to MASTER.")
alaVrrp3StatsAdvertiseRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsAdvertiseRcvd.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsAdvertiseRcvd.setDescription('The total number of VRRP advertisements received by this virtual router.')
alaVrrp3StatsAdvIntervalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsAdvIntervalErrors.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsAdvIntervalErrors.setDescription('The total number of VRRP advertisement packets received for which the advertisement interval is different than the one configured for the local virtual router.')
alaVrrp3StatsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsIpTtlErrors.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsIpTtlErrors.setDescription('The total number of VRRP packets received by the virtual router with IP TTL (Time-To-Live) not equal to 255. It also indicates the number of VRRPv3 packets received by the virtual router with IPv6 hop limit not equal to 255.')
alaVrrp3StatsPriZeroPktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsPriZeroPktsRcvd.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsPriZeroPktsRcvd.setDescription("The total number of VRRP packets received by the virtual router with a priority of '0'.")
alaVrrp3StatsPriZeroPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsPriZeroPktsSent.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsPriZeroPktsSent.setDescription("The total number of VRRP packets sent by the virtual router with a priority of '0'.")
alaVrrp3StatsInvldTypePktsRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsInvldTypePktsRcvd.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsInvldTypePktsRcvd.setDescription("The number of VRRP packets received by the virtual router with an invalid value in the 'type' field.")
alaVrrp3StatsAddressListErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsAddressListErrors.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsAddressListErrors.setDescription('The total number of packets received for which the address list does not match the locally configured list for the virtual router.')
alaVrrp3StatsInvldAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsInvldAuthType.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsInvldAuthType.setDescription("The total number of packets received with 'Auth Type' not equal to Authentication Type 0, No Authentication. This is required only for rows indicating VRRP over IPv4. This object can be sparse and should not be implemented for rows indicating VRRP for Ipv6.")
alaVrrp3StatsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 2, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaVrrp3StatsPacketLengthErrors.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsPacketLengthErrors.setDescription('The total number of packets received with a packet length less than the length of the VRRP header.')
alaVrrp3Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 0))
alaVrrp3TrapNewMasterReason = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("priority", 0), ("preempted", 1), ("masterNoResponse", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaVrrp3TrapNewMasterReason.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3TrapNewMasterReason.setDescription('This indicates the reason for NewMaster trap. Used by alaVrrp3TrapNewMaster trap.')
alaVrrp3TrapProtoErrReason = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("hopLimitError", 0), ("versionError", 1), ("checksumError", 2), ("vridError", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alaVrrp3TrapProtoErrReason.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3TrapProtoErrReason.setDescription('This indicates the reason for protocol error trap. Used by alaVrrp3TrapProtoError trap.')
alaVrrp3TrapNewMaster = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 0, 1)).setObjects(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddrType"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddr"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapNewMasterReason"))
if mibBuilder.loadTexts: alaVrrp3TrapNewMaster.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3TrapNewMaster.setDescription("The newMaster trap indicates that the sending agent has transitioned to 'Master' state.")
alaVrrp3TrapProtoError = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 0, 2)).setObjects(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapProtoErrReason"))
if mibBuilder.loadTexts: alaVrrp3TrapProtoError.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3TrapProtoError.setDescription('The error trap indicates that the sending agent has encountered the protocol error indicated by ErrorReason.')
alaVrrp3MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 1))
alaVrrp3MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2))
alaVrrp3MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 1, 1)).setObjects(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperGroup"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsGroup"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapInfoGroup"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVrrp3MIBCompliance = alaVrrp3MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3MIBCompliance.setDescription('The compliance statement for switches with Alcatel VRRP and implementing ALCATEL-IND1-VRRP3-MIB.')
alaVrrp3OperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 1)).setObjects(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3NotificationCntl"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVirtualMacAddr"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperState"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperAdminState"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPriority"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperVersion"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperIpAddrCount"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddrType"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperMasterIpAddr"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPrimaryIpAddrType"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPrimaryIpAddr"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperAdvInterval"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperPreemptMode"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperAcceptMode"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperUpTime"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3OperRowStatus"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3AssoIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVrrp3OperGroup = alaVrrp3OperGroup.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3OperGroup.setDescription('A collection of objects to support management of Alcatel VRRP.')
alaVrrp3StatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 2)).setObjects(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3RouterChecksumErrors"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3RouterVersionErrors"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3RouterVrIdErrors"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsBecomeMaster"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsAdvertiseRcvd"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsAdvIntervalErrors"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsPriZeroPktsRcvd"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsPriZeroPktsSent"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsInvldTypePktsRcvd"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsInvldAuthType"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsIpTtlErrors"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsAddressListErrors"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3StatsPacketLengthErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVrrp3StatsGroup = alaVrrp3StatsGroup.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3StatsGroup.setDescription('A collection of objects to support management of Alcatel VRRP.')
alaVrrp3TrapInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 3)).setObjects(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapNewMasterReason"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapProtoErrReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVrrp3TrapInfoGroup = alaVrrp3TrapInfoGroup.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3TrapInfoGroup.setDescription('A collection of objects to support management of Alcatel VRRP.')
alaVrrp3NotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 28, 2, 3, 2, 4)).setObjects(("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapNewMaster"), ("ALCATEL-IND1-VRRP3-MIB", "alaVrrp3TrapProtoError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaVrrp3NotificationsGroup = alaVrrp3NotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: alaVrrp3NotificationsGroup.setDescription('A collection of objects to support management of Alcatel VRRP.')
mibBuilder.exportSymbols("ALCATEL-IND1-VRRP3-MIB", alaVrrp3AssoIpAddr=alaVrrp3AssoIpAddr, alaVrrp3TrapInfoGroup=alaVrrp3TrapInfoGroup, alaVrrp3NotificationsGroup=alaVrrp3NotificationsGroup, alaVrrp3MIBCompliances=alaVrrp3MIBCompliances, alaVrrp3StatsPriZeroPktsSent=alaVrrp3StatsPriZeroPktsSent, alaVrrp3RouterVersionErrors=alaVrrp3RouterVersionErrors, alaVrrp3OperUpTime=alaVrrp3OperUpTime, alaVrrp3MIBCompliance=alaVrrp3MIBCompliance, alaVrrp3OperPrimaryIpAddr=alaVrrp3OperPrimaryIpAddr, alaVrrp3AssoIpAddrTable=alaVrrp3AssoIpAddrTable, alaVrrp3RouterChecksumErrors=alaVrrp3RouterChecksumErrors, alaVrrp3OperAdminState=alaVrrp3OperAdminState, alaVrrp3StatsBecomeMaster=alaVrrp3StatsBecomeMaster, alaVrrp3StatsInvldTypePktsRcvd=alaVrrp3StatsInvldTypePktsRcvd, alaVrrp3OperPreemptMode=alaVrrp3OperPreemptMode, alaVrrp3OperTable=alaVrrp3OperTable, alaVrrp3OperMasterIpAddrType=alaVrrp3OperMasterIpAddrType, alaVrrp3AssoIpAddrEntry=alaVrrp3AssoIpAddrEntry, alaVrrp3StatsGroup=alaVrrp3StatsGroup, alaVrrp3OperRowStatus=alaVrrp3OperRowStatus, alaVrrp3TrapProtoErrReason=alaVrrp3TrapProtoErrReason, PYSNMP_MODULE_ID=alcatelIND1VRRP3MIB, alaVrrp3StatsInvldAuthType=alaVrrp3StatsInvldAuthType, alaVrrp3Operations=alaVrrp3Operations, alaVrrp3RouterStatsEntry=alaVrrp3RouterStatsEntry, alaVrrp3StatsAdvertiseRcvd=alaVrrp3StatsAdvertiseRcvd, alaVrrp3TrapNewMasterReason=alaVrrp3TrapNewMasterReason, alaVrrp3OperIpVersion=alaVrrp3OperIpVersion, alaVrrp3OperMasterIpAddr=alaVrrp3OperMasterIpAddr, alaVrrp3StatsIpTtlErrors=alaVrrp3StatsIpTtlErrors, alaVrrp3NotificationCntl=alaVrrp3NotificationCntl, alaVrrp3AssoIpAddrType=alaVrrp3AssoIpAddrType, alaVrrp3TrapNewMaster=alaVrrp3TrapNewMaster, alaVrrp3OperGroup=alaVrrp3OperGroup, alaVrrp3RouterVrIdErrors=alaVrrp3RouterVrIdErrors, alaVrrp3OperVrId=alaVrrp3OperVrId, alaVrrp3OperPrimaryIpAddrType=alaVrrp3OperPrimaryIpAddrType, alaVrrp3Conformance=alaVrrp3Conformance, alaVrrp3StatsPacketLengthErrors=alaVrrp3StatsPacketLengthErrors, alaVrrp3OperPriority=alaVrrp3OperPriority, alaVrrp3OperAcceptMode=alaVrrp3OperAcceptMode, alaVrrp3Statistics=alaVrrp3Statistics, alaVrrp3RouterStatsTable=alaVrrp3RouterStatsTable, alaVrrp3OperIpAddrCount=alaVrrp3OperIpAddrCount, alaVrrp3OperEntry=alaVrrp3OperEntry, alaVrrp3StatsAddressListErrors=alaVrrp3StatsAddressListErrors, alcatelIND1VRRP3MIB=alcatelIND1VRRP3MIB, alaVrrp3StatsPriZeroPktsRcvd=alaVrrp3StatsPriZeroPktsRcvd, alaVrrp3StatsAdvIntervalErrors=alaVrrp3StatsAdvIntervalErrors, alaVrrp3OperAdvInterval=alaVrrp3OperAdvInterval, alaVrrp3Notifications=alaVrrp3Notifications, alaVrrp3OperState=alaVrrp3OperState, alaVrrp3TrapProtoError=alaVrrp3TrapProtoError, alaVrrp3MIBGroups=alaVrrp3MIBGroups, alaVrrp3OperVirtualMacAddr=alaVrrp3OperVirtualMacAddr, alaVrrp3AssoIpAddrRowStatus=alaVrrp3AssoIpAddrRowStatus, alaVrrp3OperVersion=alaVrrp3OperVersion)
