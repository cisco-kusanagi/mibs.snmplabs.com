#
# PySNMP MIB module VRRPV3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VRRPV3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:24:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, mib_2, Bits, Counter32, Gauge32, ModuleIdentity, Integer32, IpAddress, Unsigned32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "mib-2", "Bits", "Counter32", "Gauge32", "ModuleIdentity", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "iso")
TimeInterval, TextualConvention, TimeStamp, TruthValue, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "TimeStamp", "TruthValue", "RowStatus", "MacAddress", "DisplayString")
vrrpv3MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 207))
vrrpv3MIB.setRevisions(('2012-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vrrpv3MIB.setRevisionsDescriptions(('Initial version as published in RFC 6527.',))
if mibBuilder.loadTexts: vrrpv3MIB.setLastUpdated('201202130000Z')
if mibBuilder.loadTexts: vrrpv3MIB.setOrganization('IETF VRRP Working Group')
if mibBuilder.loadTexts: vrrpv3MIB.setContactInfo('WG E-Mail: vrrp@ietf.org Editor: Kalyan Tata Nokia 313 Fairchild Dr, Mountain View, CA 94043 Tata_kalyan@yahoo.com')
if mibBuilder.loadTexts: vrrpv3MIB.setDescription("This MIB describes objects used for managing Virtual Router Redundancy Protocol version 3 (VRRPv3). Copyright (c) 2012 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). This version of the MIB module is part of RFC 6527. Please see the RFC for full legal notices.")
class Vrrpv3VrIdTC(TextualConvention, Integer32):
    reference = 'RFC 5798 (Sections 3 and 5.2.3)'
    description = 'The value of the Virtual Router Identifier noted as (VRID) in RFC 5798. This, along with interface index (ifIndex) and IP version, serves to uniquely identify a virtual router on a given VRRP router.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

vrrpv3Notifications = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 0))
vrrpv3Objects = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1))
vrrpv3Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2))
vrrpv3Operations = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1, 1))
vrrpv3Statistics = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 1, 2))
vrrpv3OperationsTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 1, 1), )
if mibBuilder.loadTexts: vrrpv3OperationsTable.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsTable.setDescription("Unified Operations table for a VRRP router that consists of a sequence (i.e., one or more conceptual rows) of 'vrrpv3OperationsEntry' items each of which describe the operational characteristics of a virtual router.")
vrrpv3OperationsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"), (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"))
if mibBuilder.loadTexts: vrrpv3OperationsEntry.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsEntry.setDescription('An entry in the vrrpv3OperationsTable containing the operational characteristics of a virtual router. On a VRRP router, a given virtual router is identified by a combination of ifIndex, VRID, and the IP version. ifIndex represents an interface of the router. A row must be created with vrrpv3OperationsStatus set to initialize(1) and cannot transition to backup(2) or master(3) until vrrpv3OperationsRowStatus is transitioned to active(1). The information in this table is persistent and when written the entity SHOULD save the change to non- volatile storage.')
vrrpv3OperationsVrId = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 1), Vrrpv3VrIdTC())
if mibBuilder.loadTexts: vrrpv3OperationsVrId.setReference('RFC 4001')
if mibBuilder.loadTexts: vrrpv3OperationsVrId.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsVrId.setDescription('This object contains the Virtual Router Identifier (VRID).')
vrrpv3OperationsInetAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 2), InetAddressType())
if mibBuilder.loadTexts: vrrpv3OperationsInetAddrType.setReference('RFC 4001')
if mibBuilder.loadTexts: vrrpv3OperationsInetAddrType.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsInetAddrType.setDescription('The IP address type of Vrrpv3OperationsEntry and Vrrpv3AssociatedIpAddrEntry. This value determines the type for vrrpv3OperationsMasterIpAddr, vrrpv3OperationsPrimaryIpAddr, and vrrpv3AssociatedIpAddrAddress. ipv4(1) and ipv6(2) are the only two values supported in this MIB module.')
vrrpv3OperationsMasterIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsMasterIpAddr.setReference('RFC 5798')
if mibBuilder.loadTexts: vrrpv3OperationsMasterIpAddr.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsMasterIpAddr.setDescription("The master router's real IP address. The master router would set this address to vrrpv3OperationsPrimaryIpAddr while transitioning to master state. For backup routers, this is the IP address listed as the source in the VRRP advertisement last received by this virtual router.")
vrrpv3OperationsPrimaryIpAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPrimaryIpAddr.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsPrimaryIpAddr.setDescription("In the case where there is more than one IP Address (associated IP addresses) for a given 'ifIndex', this object is used to specify the IP address that will become the vrrpv3OperationsMasterIpAddr', should the virtual router transition from backup state to master.")
vrrpv3OperationsVirtualMacAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsVirtualMacAddr.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsVirtualMacAddr.setDescription("The virtual MAC address of the virtual router. Although this object can be derived from the 'vrrpv3OperationsVrId' object, it is defined so that it is easily obtainable by a management application and can be included in VRRP-related SNMP notifications.")
vrrpv3OperationsStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsStatus.setReference('RFC 5798')
if mibBuilder.loadTexts: vrrpv3OperationsStatus.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsStatus.setDescription("The current state of the virtual router. This object has three defined values: - 'initialize', which indicates that the virtual router is waiting for a startup event. - 'backup', which indicates that the virtual router is monitoring the availability of the master router. - 'master', which indicates that the virtual router is forwarding packets for IP addresses that are associated with this router.")
vrrpv3OperationsPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPriority.setReference('RFC 5798, Section 6.1')
if mibBuilder.loadTexts: vrrpv3OperationsPriority.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsPriority.setDescription("This object specifies the priority to be used for the virtual router master election process; higher values imply higher priority. A priority of '0', although not settable, is sent by the master router to indicate that this router has ceased to participate in VRRP, and a backup virtual router should transition to become a new master. A priority of 255 is used for the router that owns the associated IP address(es) for VRRP over IPv4 and hence is not settable. Setting the values of this object to 0 or 255 should be rejected by the agents implementing this MIB module. For example, an SNMP agent would return 'badValue(3)' when a user tries to set the values 0 or 255 for this object.")
vrrpv3OperationsAddrCount = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsAddrCount.setReference('RFC 5798, Section 6.1')
if mibBuilder.loadTexts: vrrpv3OperationsAddrCount.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsAddrCount.setDescription('The number of IP addresses that are associated with this virtual router. This number is equal to the number of rows in the vrrpv3AssociatedAddrTable that correspond to a given ifIndex/VRID/IP version.')
vrrpv3OperationsAdvInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 9), TimeInterval().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)).clone(100)).setUnits('centiseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsAdvInterval.setReference('RFC 5798, Section 6.1')
if mibBuilder.loadTexts: vrrpv3OperationsAdvInterval.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsAdvInterval.setDescription('The time interval, in centiseconds, between sending advertisement messages. Only the master router sends VRRP advertisements.')
vrrpv3OperationsPreemptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsPreemptMode.setReference('RFC 5798, Section 6.1')
if mibBuilder.loadTexts: vrrpv3OperationsPreemptMode.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsPreemptMode.setDescription('Controls whether a higher priority virtual router will preempt a lower priority master.')
vrrpv3OperationsAcceptMode = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsAcceptMode.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsAcceptMode.setDescription("Controls whether a virtual router in master state will accept packets addressed to the address owner's IPv6 address as its own if it is not the IPv6 address owner. Default is false(2). This object is not relevant for rows representing VRRP over IPv4 and should be set to false(2).")
vrrpv3OperationsUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3OperationsUpTime.setReference('RFC 5798, Section 6.1')
if mibBuilder.loadTexts: vrrpv3OperationsUpTime.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsUpTime.setDescription("This value represents the amount of time, in TimeTicks (hundredth of a second), since this virtual router (i.e., the 'vrrpv3OperationsStatus') transitioned out of 'initialize'.")
vrrpv3OperationsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3OperationsRowStatus.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsRowStatus.setDescription("The RowStatus variable should be used in accordance to installation and removal conventions for conceptual rows. To create a row in this table, a manager sets this object to either createAndGo(4) or createAndWait(5). Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the 'vrrpv3OperationsRowStatus' column will be read as notReady(3). In particular, a newly created row cannot be made active(1) until (minimally) the corresponding instance of vrrpv3OperationsInetAddrType, vrrpv3OperationsVrId, and vrrpv3OperationsPrimaryIpAddr has been set, and there is at least one active row in the 'vrrpv3AssociatedIpAddrTable' defining an associated IP address. notInService(2) should be used to administratively bring the row down. A typical order of operation to add a row is: 1. Create a row in vrrpv3OperationsTable with createAndWait(5). 2. Create one or more corresponding rows in vrrpv3AssociatedIpAddrTable. 3. Populate the vrrpv3OperationsEntry. 4. Set vrrpv3OperationsRowStatus to active(1). A typical order of operation to delete an entry is: 1. Set vrrpv3OperationsRowStatus to notInService(2). 2. Set the corresponding rows in vrrpv3AssociatedIpAddrTable to destroy(6) to delete the entry. 3. Set vrrpv3OperationsRowStatus to destroy(6) to delete the entry.")
vrrpv3AssociatedIpAddrTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 1, 2), )
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrTable.setStatus('current')
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrTable.setDescription('The table of addresses associated with each virtual router.')
vrrpv3AssociatedIpAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRPV3-MIB", "vrrpv3OperationsVrId"), (0, "VRRPV3-MIB", "vrrpv3OperationsInetAddrType"), (0, "VRRPV3-MIB", "vrrpv3AssociatedIpAddrAddress"))
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrEntry.setStatus('current')
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrEntry.setDescription("An entry in the table contains an IP address that is associated with a virtual router. The number of rows for a given IP version, VrID, and ifIndex will equal the number of IP addresses associated (e.g., backed up) by the virtual router (equivalent to 'vrrpv3OperationsIpAddrCount'). Rows in the table cannot be modified unless the value of 'vrrpv3OperationsStatus' for the corresponding entry in the vrrpv3OperationsTable has transitioned to initialize(1). The information in this table is persistent and when written the entity SHOULD save the change to non- volatile storage.")
vrrpv3AssociatedIpAddrAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 1), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrAddress.setReference('RFC 5798')
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrAddress.setStatus('current')
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrAddress.setDescription('The assigned IP addresses that a virtual router is responsible for backing up. The IP address type is determined by the value of vrrpv3OperationsInetAddrType in the index of this row.')
vrrpv3AssociatedIpAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrRowStatus.setStatus('current')
if mibBuilder.loadTexts: vrrpv3AssociatedIpAddrRowStatus.setDescription('The row status variable, used according to installation and removal conventions for conceptual rows. To create a row in this table, a manager sets this object to either createAndGo(4) or createAndWait(5). Setting this object to active(1) results in the addition of an associated address for a virtual router. Setting this object to notInService(2) results in administratively bringing down the row. Destroying the entry or setting it to destroy(6) removes the associated address from the virtual router. The use of other values is implementation-dependent. Implementations should not allow deletion of the last row corresponding to an active row in vrrpv3OperationsTable. Refer to the description of vrrpv3OperationsRowStatus for typical row creation and deletion scenarios.')
vrrpv3RouterChecksumErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterChecksumErrors.setReference('RFC 5798, Section 5.2.8')
if mibBuilder.loadTexts: vrrpv3RouterChecksumErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpv3RouterChecksumErrors.setDescription('The total number of VRRP packets received with an invalid VRRP checksum value. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3GlobalStatisticsDiscontinuityTime.')
vrrpv3RouterVersionErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterVersionErrors.setReference('RFC 5798, Section 5.2.1')
if mibBuilder.loadTexts: vrrpv3RouterVersionErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpv3RouterVersionErrors.setDescription('The total number of VRRP packets received with an unknown or unsupported version number. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3GlobalStatisticsDiscontinuityTime.')
vrrpv3RouterVrIdErrors = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3RouterVrIdErrors.setReference('RFC 5798, Section 5.2.3')
if mibBuilder.loadTexts: vrrpv3RouterVrIdErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpv3RouterVrIdErrors.setDescription('The total number of VRRP packets received with a VRID that is not valid for any virtual router on this router. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3GlobalStatisticsDiscontinuityTime.')
vrrpv3GlobalStatisticsDiscontinuityTime = MibScalar((1, 3, 6, 1, 2, 1, 207, 1, 2, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3GlobalStatisticsDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: vrrpv3GlobalStatisticsDiscontinuityTime.setDescription('The value of sysUpTime on the most recent occasion at which one of vrrpv3RouterChecksumErrors, vrrpv3RouterVersionErrors, and vrrpv3RouterVrIdErrors suffered a discontinuity. If no such discontinuities have occurred since the last re-initialization of the local management subsystem, then this object contains a zero value.')
vrrpv3StatisticsTable = MibTable((1, 3, 6, 1, 2, 1, 207, 1, 2, 5), )
if mibBuilder.loadTexts: vrrpv3StatisticsTable.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsTable.setDescription('Table of virtual router statistics.')
vrrpv3StatisticsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1), )
vrrpv3OperationsEntry.registerAugmentions(("VRRPV3-MIB", "vrrpv3StatisticsEntry"))
vrrpv3StatisticsEntry.setIndexNames(*vrrpv3OperationsEntry.getIndexNames())
if mibBuilder.loadTexts: vrrpv3StatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsEntry.setDescription('An entry in the table containing statistics information about a given virtual router.')
vrrpv3StatisticsMasterTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsMasterTransitions.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsMasterTransitions.setDescription("The total number of times that this virtual router's state has transitioned to master state. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsNewMasterReason = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notMaster", 0), ("priority", 1), ("preempted", 2), ("masterNoResponse", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsNewMasterReason.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsNewMasterReason.setDescription('This indicates the reason for the virtual router to transition to master state. If the virtual router never transitioned to master state, the value of this object is notMaster(0). Otherwise, this indicates the reason this virtual router transitioned to master state the last time. Used by vrrpv3NewMaster notification.')
vrrpv3StatisticsRcvdAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdAdvertisements.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdAdvertisements.setDescription('The total number of VRRP advertisements received by this virtual router. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.')
vrrpv3StatisticsAdvIntervalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsAdvIntervalErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsAdvIntervalErrors.setDescription('The total number of VRRP advertisement packets received for which the advertisement interval is different from the vrrpv3OperationsAdvInterval configured on this virtual router. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.')
vrrpv3StatisticsIpTtlErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsIpTtlErrors.setReference('RFC 5798, Section 5.1.1.3')
if mibBuilder.loadTexts: vrrpv3StatisticsIpTtlErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsIpTtlErrors.setDescription('The total number of VRRP packets received by the virtual router with IPv4 TTL (for VRRP over IPv4) or IPv6 Hop Limit (for VRRP over IPv6) not equal to 255. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.')
vrrpv3StatisticsProtoErrReason = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("noError", 0), ("ipTtlError", 1), ("versionError", 2), ("checksumError", 3), ("vrIdError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsProtoErrReason.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsProtoErrReason.setDescription('This indicates the reason for the last protocol error. This SHOULD be set to noError(0) when no protocol errors are encountered. Used by vrrpv3ProtoError notification.')
vrrpv3StatisticsRcvdPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdPriZeroPackets.setReference('RFC 5798, Section 5.2.4')
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdPriZeroPackets.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdPriZeroPackets.setDescription("The total number of VRRP packets received by the virtual router with a priority of '0'. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsSentPriZeroPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsSentPriZeroPackets.setReference('RFC 5798, Section 5.2.4')
if mibBuilder.loadTexts: vrrpv3StatisticsSentPriZeroPackets.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsSentPriZeroPackets.setDescription("The total number of VRRP packets sent by the virtual router with a priority of '0'. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsRcvdInvalidTypePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdInvalidTypePackets.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsRcvdInvalidTypePackets.setDescription("The number of VRRP packets received by the virtual router with an invalid value in the 'type' field. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.")
vrrpv3StatisticsAddressListErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsAddressListErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsAddressListErrors.setDescription('The total number of packets received for which the address list does not match the locally configured list for the virtual router. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.')
vrrpv3StatisticsPacketLengthErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsPacketLengthErrors.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsPacketLengthErrors.setDescription('The total number of packets received with a packet length less than the length of the VRRP header. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of vrrpv3StatisticsRowDiscontinuityTime.')
vrrpv3StatisticsRowDiscontinuityTime = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRowDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsRowDiscontinuityTime.setDescription("The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity. If no such discontinuities have occurred since the last re-initialization of the local management subsystem, then this object contains a zero value.")
vrrpv3StatisticsRefreshRate = MibTableColumn((1, 3, 6, 1, 2, 1, 207, 1, 2, 5, 1, 13), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: vrrpv3StatisticsRefreshRate.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsRefreshRate.setDescription('The minimum reasonable polling interval for this entry. This object provides an indication of the minimum amount of time required to update the counters in this entry.')
vrrpv3NewMaster = NotificationType((1, 3, 6, 1, 2, 1, 207, 0, 1)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsMasterIpAddr"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"))
if mibBuilder.loadTexts: vrrpv3NewMaster.setStatus('current')
if mibBuilder.loadTexts: vrrpv3NewMaster.setDescription('The newMaster notification indicates that the sending agent has transitioned to master state.')
vrrpv3ProtoError = NotificationType((1, 3, 6, 1, 2, 1, 207, 0, 2)).setObjects(("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"))
if mibBuilder.loadTexts: vrrpv3ProtoError.setStatus('current')
if mibBuilder.loadTexts: vrrpv3ProtoError.setDescription('The notification indicates that the sending agent has encountered the protocol error indicated by vrrpv3StatisticsProtoErrReason.')
vrrpv3Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2, 1))
vrrpv3Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 207, 2, 2))
vrrpv3FullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 207, 2, 1, 1)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsGroup"), ("VRRPV3-MIB", "vrrpv3StatisticsGroup"), ("VRRPV3-MIB", "vrrpv3InfoGroup"), ("VRRPV3-MIB", "vrrpv3NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3FullCompliance = vrrpv3FullCompliance.setStatus('current')
if mibBuilder.loadTexts: vrrpv3FullCompliance.setDescription('The compliance statement')
vrrpv3ReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 207, 2, 1, 2)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsGroup"), ("VRRPV3-MIB", "vrrpv3StatisticsGroup"), ("VRRPV3-MIB", "vrrpv3StatisticsDiscontinuityGroup"), ("VRRPV3-MIB", "vrrpv3InfoGroup"), ("VRRPV3-MIB", "vrrpv3NotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3ReadOnlyCompliance = vrrpv3ReadOnlyCompliance.setStatus('current')
if mibBuilder.loadTexts: vrrpv3ReadOnlyCompliance.setDescription('When this MIB module is implemented without support for read-create (i.e., in read-only mode), then such an implementation can claim read-only compliance. Such a device can then be monitored, but cannot be configured with this MIB.')
vrrpv3OperationsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 1)).setObjects(("VRRPV3-MIB", "vrrpv3OperationsVirtualMacAddr"), ("VRRPV3-MIB", "vrrpv3OperationsStatus"), ("VRRPV3-MIB", "vrrpv3OperationsPriority"), ("VRRPV3-MIB", "vrrpv3OperationsMasterIpAddr"), ("VRRPV3-MIB", "vrrpv3OperationsAdvInterval"), ("VRRPV3-MIB", "vrrpv3OperationsPreemptMode"), ("VRRPV3-MIB", "vrrpv3OperationsAcceptMode"), ("VRRPV3-MIB", "vrrpv3OperationsUpTime"), ("VRRPV3-MIB", "vrrpv3OperationsRowStatus"), ("VRRPV3-MIB", "vrrpv3OperationsAddrCount"), ("VRRPV3-MIB", "vrrpv3OperationsPrimaryIpAddr"), ("VRRPV3-MIB", "vrrpv3AssociatedIpAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3OperationsGroup = vrrpv3OperationsGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpv3OperationsGroup.setDescription('Conformance group for VRRPv3 operations.')
vrrpv3StatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 2)).setObjects(("VRRPV3-MIB", "vrrpv3RouterChecksumErrors"), ("VRRPV3-MIB", "vrrpv3RouterVersionErrors"), ("VRRPV3-MIB", "vrrpv3RouterVrIdErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsMasterTransitions"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdAdvertisements"), ("VRRPV3-MIB", "vrrpv3StatisticsAdvIntervalErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdPriZeroPackets"), ("VRRPV3-MIB", "vrrpv3StatisticsSentPriZeroPackets"), ("VRRPV3-MIB", "vrrpv3StatisticsRcvdInvalidTypePackets"), ("VRRPV3-MIB", "vrrpv3StatisticsIpTtlErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"), ("VRRPV3-MIB", "vrrpv3StatisticsAddressListErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsPacketLengthErrors"), ("VRRPV3-MIB", "vrrpv3StatisticsRowDiscontinuityTime"), ("VRRPV3-MIB", "vrrpv3StatisticsRefreshRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3StatisticsGroup = vrrpv3StatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsGroup.setDescription('Conformance group for VRRPv3 statistics.')
vrrpv3StatisticsDiscontinuityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 3)).setObjects(("VRRPV3-MIB", "vrrpv3GlobalStatisticsDiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3StatisticsDiscontinuityGroup = vrrpv3StatisticsDiscontinuityGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpv3StatisticsDiscontinuityGroup.setDescription('Objects providing information about counter discontinuities.')
vrrpv3InfoGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 4)).setObjects(("VRRPV3-MIB", "vrrpv3StatisticsProtoErrReason"), ("VRRPV3-MIB", "vrrpv3StatisticsNewMasterReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3InfoGroup = vrrpv3InfoGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpv3InfoGroup.setDescription('Conformance group for objects contained in VRRPv3 notifications.')
vrrpv3NotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 207, 2, 2, 5)).setObjects(("VRRPV3-MIB", "vrrpv3NewMaster"), ("VRRPV3-MIB", "vrrpv3ProtoError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vrrpv3NotificationsGroup = vrrpv3NotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: vrrpv3NotificationsGroup.setDescription('The VRRP MIB Notification Group.')
mibBuilder.exportSymbols("VRRPV3-MIB", Vrrpv3VrIdTC=Vrrpv3VrIdTC, vrrpv3OperationsPrimaryIpAddr=vrrpv3OperationsPrimaryIpAddr, vrrpv3AssociatedIpAddrTable=vrrpv3AssociatedIpAddrTable, vrrpv3StatisticsNewMasterReason=vrrpv3StatisticsNewMasterReason, vrrpv3Conformance=vrrpv3Conformance, vrrpv3StatisticsRowDiscontinuityTime=vrrpv3StatisticsRowDiscontinuityTime, vrrpv3OperationsAcceptMode=vrrpv3OperationsAcceptMode, vrrpv3RouterVrIdErrors=vrrpv3RouterVrIdErrors, vrrpv3MIB=vrrpv3MIB, vrrpv3StatisticsAdvIntervalErrors=vrrpv3StatisticsAdvIntervalErrors, vrrpv3AssociatedIpAddrEntry=vrrpv3AssociatedIpAddrEntry, vrrpv3OperationsPriority=vrrpv3OperationsPriority, vrrpv3NewMaster=vrrpv3NewMaster, vrrpv3OperationsMasterIpAddr=vrrpv3OperationsMasterIpAddr, vrrpv3InfoGroup=vrrpv3InfoGroup, vrrpv3OperationsEntry=vrrpv3OperationsEntry, vrrpv3Compliances=vrrpv3Compliances, vrrpv3AssociatedIpAddrRowStatus=vrrpv3AssociatedIpAddrRowStatus, vrrpv3StatisticsTable=vrrpv3StatisticsTable, vrrpv3OperationsInetAddrType=vrrpv3OperationsInetAddrType, vrrpv3OperationsVrId=vrrpv3OperationsVrId, vrrpv3FullCompliance=vrrpv3FullCompliance, vrrpv3StatisticsSentPriZeroPackets=vrrpv3StatisticsSentPriZeroPackets, vrrpv3OperationsTable=vrrpv3OperationsTable, vrrpv3StatisticsAddressListErrors=vrrpv3StatisticsAddressListErrors, vrrpv3NotificationsGroup=vrrpv3NotificationsGroup, vrrpv3Objects=vrrpv3Objects, vrrpv3StatisticsRcvdAdvertisements=vrrpv3StatisticsRcvdAdvertisements, vrrpv3OperationsUpTime=vrrpv3OperationsUpTime, vrrpv3OperationsVirtualMacAddr=vrrpv3OperationsVirtualMacAddr, vrrpv3RouterChecksumErrors=vrrpv3RouterChecksumErrors, vrrpv3OperationsAdvInterval=vrrpv3OperationsAdvInterval, vrrpv3OperationsStatus=vrrpv3OperationsStatus, vrrpv3StatisticsIpTtlErrors=vrrpv3StatisticsIpTtlErrors, vrrpv3StatisticsRcvdPriZeroPackets=vrrpv3StatisticsRcvdPriZeroPackets, vrrpv3ReadOnlyCompliance=vrrpv3ReadOnlyCompliance, vrrpv3GlobalStatisticsDiscontinuityTime=vrrpv3GlobalStatisticsDiscontinuityTime, vrrpv3StatisticsRefreshRate=vrrpv3StatisticsRefreshRate, vrrpv3Groups=vrrpv3Groups, vrrpv3OperationsGroup=vrrpv3OperationsGroup, vrrpv3RouterVersionErrors=vrrpv3RouterVersionErrors, vrrpv3Notifications=vrrpv3Notifications, vrrpv3Operations=vrrpv3Operations, vrrpv3StatisticsDiscontinuityGroup=vrrpv3StatisticsDiscontinuityGroup, PYSNMP_MODULE_ID=vrrpv3MIB, vrrpv3StatisticsGroup=vrrpv3StatisticsGroup, vrrpv3Statistics=vrrpv3Statistics, vrrpv3StatisticsRcvdInvalidTypePackets=vrrpv3StatisticsRcvdInvalidTypePackets, vrrpv3AssociatedIpAddrAddress=vrrpv3AssociatedIpAddrAddress, vrrpv3ProtoError=vrrpv3ProtoError, vrrpv3OperationsAddrCount=vrrpv3OperationsAddrCount, vrrpv3OperationsRowStatus=vrrpv3OperationsRowStatus, vrrpv3StatisticsEntry=vrrpv3StatisticsEntry, vrrpv3StatisticsPacketLengthErrors=vrrpv3StatisticsPacketLengthErrors, vrrpv3StatisticsProtoErrReason=vrrpv3StatisticsProtoErrReason, vrrpv3OperationsPreemptMode=vrrpv3OperationsPreemptMode, vrrpv3StatisticsMasterTransitions=vrrpv3StatisticsMasterTransitions)