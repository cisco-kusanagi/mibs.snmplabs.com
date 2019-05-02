#
# PySNMP MIB module DNOS-ROUTE-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-ROUTE-POLICY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:52:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
fastPathRouting, = mibBuilder.importSymbols("DNOS-ROUTING-MIB", "fastPathRouting")
InterfaceIndexOrZero, ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Integer32, Counter32, ObjectIdentity, MibIdentifier, Bits, iso, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "iso", "Counter64", "Unsigned32")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
fastPathRoutePolicy = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20))
if mibBuilder.loadTexts: fastPathRoutePolicy.setLastUpdated('201210010000Z')
if mibBuilder.loadTexts: fastPathRoutePolicy.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastPathRoutePolicy.setContactInfo('')
if mibBuilder.loadTexts: fastPathRoutePolicy.setDescription('The MIB definitions for Route Policy system.')
class FastpathRoutePolicyAction(TextualConvention, Integer32):
    description = 'Determines whether a Route Map statement should be permitted or denied.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("permit", 1), ("deny", 2))

class FastpathRoutePolicyStmtIpPrecedence(TextualConvention, Integer32):
    description = 'Possible values of IP precedence that can be configured in a route-map statement.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("routine", 0), ("priority", 1), ("immediate", 2), ("flash", 3), ("flash-override", 4), ("critical", 5), ("internet", 6), ("network", 7), ("invalid", 8))

fastpathRoutePolicyNameTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1), )
if mibBuilder.loadTexts: fastpathRoutePolicyNameTable.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyNameTable.setDescription('Table to configure or fetch current list of route-map statements')
fastpathRoutePolicyNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1), ).setIndexNames((0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyName"), (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtActionType"), (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicySequence"))
if mibBuilder.loadTexts: fastpathRoutePolicyNameEntry.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyNameEntry.setDescription('Each entry in this table corresponds to a route-map statement')
fastpathRoutePolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fastpathRoutePolicyName.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyName.setDescription('The name of a Route Map statement.')
fastpathRoutePolicyStmtActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 2), FastpathRoutePolicyAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtActionType.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtActionType.setDescription('The action associated with this route-map statement. This can be either Permit/Deny ')
fastpathRoutePolicySequence = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fastpathRoutePolicySequence.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicySequence.setDescription('Route Maps are linked together using sequence numbers. All Route Maps with the same index and with different sequence numbers are linked together and processed in order of increasing sequence number.')
fastpathRoutePolicyNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fastpathRoutePolicyNameRowStatus.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyNameRowStatus.setDescription('Controls creation and deletion of Row Status entries.')
fastpathRoutePolicyStamentTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2), )
if mibBuilder.loadTexts: fastpathRoutePolicyStamentTable.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStamentTable.setDescription('Table to configure match or set statements in a route-map statement.')
fastpathRoutePolicyStatementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1), ).setIndexNames((0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtName"), (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtSeqNum"), (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyStmtAction"))
if mibBuilder.loadTexts: fastpathRoutePolicyStatementEntry.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStatementEntry.setDescription('Each entry describes match and set terms in a route-map statement if configured')
fastpathRoutePolicyStmtName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: fastpathRoutePolicyStmtName.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtName.setDescription('The name of a Route Map.')
fastpathRoutePolicyStmtSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSeqNum.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSeqNum.setDescription('Route Maps are linked together using sequence numbers. All Route Maps with the same index and with different sequence numbers are linked together and processed in order of increasing sequence number.')
fastpathRoutePolicyStmtAction = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 3), FastpathRoutePolicyAction())
if mibBuilder.loadTexts: fastpathRoutePolicyStmtAction.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtAction.setDescription('The action associated with this route-map statement. This can be either Permit/Deny ')
fastpathRoutePolicyStmtMatchIpv4AclList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchIpv4AclList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchIpv4AclList.setDescription('The string containing a list of IPv4 ACLs. This list contains either IPV4 standard ACL/IPV4 extended ACL/ named IPv4 ACL. In a single match statement, up to a maximum of 16 IPV4 ACLs can be included. ')
fastpathRoutePolicyStmtMatchIpv4AclDelList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchIpv4AclDelList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchIpv4AclDelList.setDescription('The string containing a list of IPv4 ACLs. This list contains either IPV4 standard ACL/IPV4 extended ACL/ named IPv4 ACL. In a single match statement, up to a maximum of 16 IPV4 ACLs can be included.This list is used to delete already configured match list of IPv4 ACLs in route-map statement.Earlier this list should have configured through MIB object fastpathRoutePolicyStmtMatchIpv4AclList ')
fastpathRoutePolicyStmtMatchMacAclList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchMacAclList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchMacAclList.setDescription('The string containing a list of MAC ACLs. This list contains upto 16 MAC ACL names that can be included in a match statement. ')
fastpathRoutePolicyStmtMatchMacAclDelList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchMacAclDelList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchMacAclDelList.setDescription('The string containing a list of MAC ACLs. This list contains upto 16 MAC ACL names that can be included in a match statement. This MIB object is used to delete MAC ACL lists matched in a route-map statement via fastpathRoutePolicyStmtMatchMacAclList. ')
fastpathRoutePolicyStmtMatchPacketLengthRangeMin = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchPacketLengthRangeMin.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchPacketLengthRangeMin.setDescription('Minimum value in the packet length range in a match length term. A value of zero is used to disable/remove minimum length configuration. ')
fastpathRoutePolicyStmtMatchPacketLengthRangeMax = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchPacketLengthRangeMax.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtMatchPacketLengthRangeMax.setDescription('Maximum value in the packet length range in a match length term. A value of zero is used to disable/remove maximum length configuration. ')
fastpathRoutePolicyStmtSetIpNextHopList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIpNextHopList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIpNextHopList.setDescription('The string containing a list of next-hop IP addresses. Upto a maximum of 16 IP addresses can be specified ')
fastpathRoutePolicyStmtSetIpNextHopDelList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIpNextHopDelList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIpNextHopDelList.setDescription('The string containing a list of next-hop IP addresses. Upto a maximum of 16 IP addresses can be specified.This MIB object is used to delete IP next-hop list configured via fastpathRoutePolicyStmtSetIpNextHopList ')
fastpathRoutePolicyStmtSetDefaultIpNextHopList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 12), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetDefaultIpNextHopList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetDefaultIpNextHopList.setDescription('The string containing a list of default next-hop IP addresses. Upto a maximum of 16 IP addresses can be specified ')
fastpathRoutePolicyStmtSetDefaultIpNextHopDelList = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetDefaultIpNextHopDelList.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetDefaultIpNextHopDelList.setDescription('The string containing a list of default next-hop IP addresses. Upto a maximum of 16 IP addresses can be specified.This MIB object is used to delete IP default next-hop list configured via fastpathRoutePolicyStmtSetDefaultIpNextHopList ')
fastpathRoutePolicyStmtSetIpPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 14), FastpathRoutePolicyStmtIpPrecedence()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIpPrecedence.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIpPrecedence.setDescription('IP Precedence value to be remarked. This is specified through set clause in route-map statement. In order to remove configured precedence value, use invalid(8) option. ')
fastpathRoutePolicyStmtSetIntfNull0 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 2, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIntfNull0.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyStmtSetIntfNull0.setDescription('Specifying null0 as an interface in a route-map statement')
fastpathRoutePolicyIfTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3), )
if mibBuilder.loadTexts: fastpathRoutePolicyIfTable.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyIfTable.setDescription('A table of interfaces on which route-map is applied.')
fastpathRoutePolicyIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1), ).setIndexNames((0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyIfIndex"), (0, "DNOS-ROUTE-POLICY-MIB", "fastpathRoutePolicyIfName"))
if mibBuilder.loadTexts: fastpathRoutePolicyIfEntry.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyIfEntry.setDescription('')
fastpathRoutePolicyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fastpathRoutePolicyIfIndex.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyIfIndex.setDescription('Interface to which route-map needs to be applied or Interface from which route-map needs to be removed.')
fastpathRoutePolicyIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fastpathRoutePolicyIfName.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyIfName.setDescription('The name of a Route Map.')
fastpathRoutePolicyIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 2, 20, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fastpathRoutePolicyIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: fastpathRoutePolicyIfRowStatus.setDescription('Controls creation and deletion of Row Status entries.')
mibBuilder.exportSymbols("DNOS-ROUTE-POLICY-MIB", fastpathRoutePolicyStmtActionType=fastpathRoutePolicyStmtActionType, fastpathRoutePolicyStmtMatchIpv4AclList=fastpathRoutePolicyStmtMatchIpv4AclList, fastpathRoutePolicyStmtSetDefaultIpNextHopDelList=fastpathRoutePolicyStmtSetDefaultIpNextHopDelList, fastpathRoutePolicyStmtMatchMacAclList=fastpathRoutePolicyStmtMatchMacAclList, fastpathRoutePolicyStmtSetDefaultIpNextHopList=fastpathRoutePolicyStmtSetDefaultIpNextHopList, fastpathRoutePolicyIfName=fastpathRoutePolicyIfName, fastpathRoutePolicyNameEntry=fastpathRoutePolicyNameEntry, fastpathRoutePolicyStamentTable=fastpathRoutePolicyStamentTable, fastpathRoutePolicyIfRowStatus=fastpathRoutePolicyIfRowStatus, fastpathRoutePolicyStmtSetIpPrecedence=fastpathRoutePolicyStmtSetIpPrecedence, fastpathRoutePolicyIfTable=fastpathRoutePolicyIfTable, fastpathRoutePolicyStatementEntry=fastpathRoutePolicyStatementEntry, fastpathRoutePolicyName=fastpathRoutePolicyName, fastpathRoutePolicyNameRowStatus=fastpathRoutePolicyNameRowStatus, fastpathRoutePolicyNameTable=fastpathRoutePolicyNameTable, fastpathRoutePolicyStmtMatchIpv4AclDelList=fastpathRoutePolicyStmtMatchIpv4AclDelList, fastpathRoutePolicySequence=fastpathRoutePolicySequence, fastpathRoutePolicyStmtMatchMacAclDelList=fastpathRoutePolicyStmtMatchMacAclDelList, fastpathRoutePolicyIfIndex=fastpathRoutePolicyIfIndex, fastpathRoutePolicyStmtSetIntfNull0=fastpathRoutePolicyStmtSetIntfNull0, PYSNMP_MODULE_ID=fastPathRoutePolicy, fastpathRoutePolicyStmtName=fastpathRoutePolicyStmtName, fastpathRoutePolicyStmtSetIpNextHopDelList=fastpathRoutePolicyStmtSetIpNextHopDelList, fastpathRoutePolicyStmtSeqNum=fastpathRoutePolicyStmtSeqNum, fastpathRoutePolicyIfEntry=fastpathRoutePolicyIfEntry, fastpathRoutePolicyStmtSetIpNextHopList=fastpathRoutePolicyStmtSetIpNextHopList, fastpathRoutePolicyStmtAction=fastpathRoutePolicyStmtAction, fastPathRoutePolicy=fastPathRoutePolicy, FastpathRoutePolicyStmtIpPrecedence=FastpathRoutePolicyStmtIpPrecedence, fastpathRoutePolicyStmtMatchPacketLengthRangeMax=fastpathRoutePolicyStmtMatchPacketLengthRangeMax, fastpathRoutePolicyStmtMatchPacketLengthRangeMin=fastpathRoutePolicyStmtMatchPacketLengthRangeMin, FastpathRoutePolicyAction=FastpathRoutePolicyAction)
