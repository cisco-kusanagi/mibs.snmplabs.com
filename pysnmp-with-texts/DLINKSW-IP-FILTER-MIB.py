#
# PySNMP MIB module DLINKSW-IP-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINKSW-IP-FILTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:50:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
InetAddressPrefixLength, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Integer32, NotificationType, Unsigned32, Gauge32, ModuleIdentity, ObjectIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Integer32", "NotificationType", "Unsigned32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Counter32", "Bits")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
dlinkSwIPFilterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 117))
dlinkSwIPFilterMIB.setRevisions(('2016-06-08 00:00', '2016-06-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwIPFilterMIB.setRevisionsDescriptions(('This is the first version of the MIB file for configuring IP filter.', 'Add dPrefixListTable, dPrefixListRuleTable and dPrefixListDescTable.',))
if mibBuilder.loadTexts: dlinkSwIPFilterMIB.setLastUpdated('201606210000Z')
if mibBuilder.loadTexts: dlinkSwIPFilterMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwIPFilterMIB.setContactInfo(' D-Link Corporation Postal: No. 289, Sinhu 3rd Rd., Neihu District, Taipei City 114, Taiwan, R.O.C Tel: +886-2-66000123 E-mail: tsd@dlink.com.tw ')
if mibBuilder.loadTexts: dlinkSwIPFilterMIB.setDescription('This MIB module defines objects for IP filter.')
dIPFilterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 117, 0))
dIPFilterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 117, 1))
dIPFilterConform = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 117, 2))
dRouteMapTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1), )
if mibBuilder.loadTexts: dRouteMapTable.setStatus('current')
if mibBuilder.loadTexts: dRouteMapTable.setDescription('This table contains route-map name.')
dRouteMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dRouteMapName"))
if mibBuilder.loadTexts: dRouteMapEntry.setStatus('current')
if mibBuilder.loadTexts: dRouteMapEntry.setDescription('Each entry is a specific name of a route map.')
dRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: dRouteMapName.setStatus('current')
if mibBuilder.loadTexts: dRouteMapName.setDescription('The name of the route map.')
dRouteMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 1, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dRouteMapRowStatus.setStatus('current')
if mibBuilder.loadTexts: dRouteMapRowStatus.setDescription('This object indicates the status of the route-map. Only createAndGo(4) and destroy(6) are supported.')
dRouteMapSeqTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2), )
if mibBuilder.loadTexts: dRouteMapSeqTable.setStatus('current')
if mibBuilder.loadTexts: dRouteMapSeqTable.setDescription('This table contains entries for route maps instances.')
dRouteMapSeqEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dRouteMapName"), (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapSeqNum"))
if mibBuilder.loadTexts: dRouteMapSeqEntry.setStatus('current')
if mibBuilder.loadTexts: dRouteMapSeqEntry.setDescription('Each entry is a specific sequence of a route map.')
dRouteMapSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: dRouteMapSeqNum.setStatus('current')
if mibBuilder.loadTexts: dRouteMapSeqNum.setDescription('Multiple entries of the same route map can be created by assigning a different sequence number to it. Each instance is identified by the route map name and the sequence number. The value of the sequence number associated with the particular route map instance determines the order in which the routing protocol evaluates routes; the instance of having lowest sequence number is evaluated first. If the routes pass all the match conditions specified in the lowest-numbered instance, and if all set clause elements are successfully configured, then no other instance of the route map is considered. However, any routes that do not pass all the match conditions are evaluated against the next instance of the route map.')
dRouteMapSeqMatchAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dRouteMapSeqMatchAction.setStatus('current')
if mibBuilder.loadTexts: dRouteMapSeqMatchAction.setDescription('Indicates the action performed by this route map instance.')
dRouteMapSeqRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 2, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dRouteMapSeqRowStatus.setStatus('current')
if mibBuilder.loadTexts: dRouteMapSeqRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention. The writable columns in a row cannot be changed if the row is active. In other words, once created, dRouteMapMatchAction cannot be modified directly. It is required to destroy the instance and then create it with the new value. Before configure match or set a clause/element, it is required to create the same route map instance. Deletion of the route map instance will also delete all the clause elements confgured which associate the deleted route map.')
dRouteMapClauseTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3), )
if mibBuilder.loadTexts: dRouteMapClauseTable.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseTable.setDescription('This table contains entries for instances of the route map clause elements.')
dRouteMapClauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dRouteMapName"), (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapSeqNum"), (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapClauseTypeId"), (0, "DLINKSW-IP-FILTER-MIB", "dRouteMapClauseSubId"))
if mibBuilder.loadTexts: dRouteMapClauseEntry.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseEntry.setDescription('Each entry describes the characteristics of one route map clause element instance.')
dRouteMapClauseTypeId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 129, 131, 136, 137, 139, 140, 141, 142, 143, 144))).clone(namedValues=NamedValues(("matchIpAccessList", 1), ("matchIpPrefixList", 2), ("matchIpv6AccessList", 3), ("matchAsPath", 4), ("matchCommunity", 5), ("macthIpNexthop", 7), ("matchIpNexthopPrefixList", 8), ("matchMetric", 9), ("matchInterface", 10), ("matchRouteType", 11), ("matchIpRouteSource", 12), ("matchIpv6Nexthop", 13), ("matchIpv6NexthopPrefixList", 14), ("matchIpv6PrefixList", 15), ("setIpNexthop", 129), ("setIpv6Nexthop", 131), ("setAsPath", 136), ("setCommunity", 137), ("setMetric", 139), ("setLocalPreference", 140), ("setOrigin", 141), ("setWeight", 142), ("setDampening", 143), ("setMetricType", 144))))
if mibBuilder.loadTexts: dRouteMapClauseTypeId.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseTypeId.setDescription("The type of match or set command in this entry. A route map entry can contain multiple match and set statements. To match a route against a route map entry, all of the match clause elements in a route map sequence must be satisfied. When a route map entry is matched, all the set clause elements in the sequence will be performed (if applicable) for a 'permit' sequence. The valid values and ranges of dRouteMapClauseAddOption and dRouteMapClauseElementValue depends on this object. Please refer to the dRouteMapClauseRowStatus object's DESCRIPTION for details.")
dRouteMapClauseSubId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dRouteMapClauseSubId.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseSubId.setDescription('Indicates the clause element sub ID. Because for some clause types (e.g. setIpNexthop), multiple instances can be created, this object is used solely to distinguish specific instance of the element. If the created instance has same dRouteMapName, dRouteMapSeqNum, dRouteMapClauseTypeId and dRouteMapClauseElementValue as the entry exists in the dRouteMapClauseTable,the creation will be rejected. This value is determined by choosing the next available by walking the table and may change across system reboots.')
dRouteMapClauseAddOption = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 0), ("exact", 1), ("additive", 2), ("communityNone", 3))).clone('notApplicable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dRouteMapClauseAddOption.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseAddOption.setDescription("This indicates the additional option selected along with the main option (dRouteMapClauseTypeId) whenever it applies. For more information on how to map this object value to each value, refer to the route-map clauses table in the dRouteMapClauseRowStatus object's DESCRIPTION.")
dRouteMapClauseElementValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dRouteMapClauseElementValue.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseElementValue.setDescription("This represents match and set clauses' variable element instance values in character string form. Whatever may be the data type of the attribute element instance value, it is always interpreted as a set of characters for both configuration and display purposes. It is up to the user to know the element's data type mapping in order to input the correct value while configuring. Refer to the route-map clauses table in the dRouteMapClauseRowStatus object descrption for detailed information.")
dRouteMapClauseRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 3, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dRouteMapClauseRowStatus.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseRowStatus.setDescription("Controls creation/deletion of entries in this table according to the RowStatus textual convention. The writable columns in a row cannot be changed if the row is active. In other words, the table entry elements may not be modified. To create/delete an entry in this table, the following entry objects MUST be explicitly configured: dRouteMapClauseRowStatus dRouteMapClauseElementValue Make sure the corresponding route map(s) are created before configuring their corresponding clause elements. The table below explains how to determine the values and ranges of dRouteMapClauseAddOption and dRouteMapClauseElementValue. Clause element configuration table ==================================================== Clause Type Addtional Option Element Value dRouteMapClauseTypeId dRouteMapClauseAddOption dRouteMapClauseElementValue ======================= ========================== ================== matchIpAccessList notApplicable DisplayString (SIZE(1..32)) matchIpPrefixList notApplicable DisplayString (SIZE(1..32)) matchIpv6AccessList notApplicable DisplayString (SIZE(1..32)) matchIpv6PrefixList notApplicable DisplayString (SIZE(1..32)) matchAsPath notApplicable DisplayString (SIZE(1..32)) matchCommunity exact/ DisplayString (SIZE(1..32)) notApplicable DisplayString (SIZE(1..32)) macthIpNexthop notApplicable DisplayString (SIZE(1..32)) matchIpNexthopPrefixList notApplicable DisplayString (SIZE(1..32)) matchIpv6Nexthop notApplicable DisplayString (SIZE(1..32)) matchIpv6NexthopPrefixList notApplicable DisplayString (SIZE(1..32)) matchMetric notApplicable DisplayString (SIZE(1..32)) matchInterface notApplicable DisplayString (SIZE(1..32)) matchRouteType notApplicable DisplayString (SIZE(1..32)) matchIpRouteSource notApplicable DisplayString (SIZE(1..32)) setIpNexthop notApplicable InetAddressIPv4 setIpv6Nexthop notApplicable InetAddressIPv6 setAsPath notApplicable DisplayString (SIZE(1..32)) setCommunity(Note#1) additive/ DisplayString (SIZE(1..32)) communityNone zero-length string notApplicable DisplayString (SIZE(1..32)) setMetric notApplicable Unsigned32 setLocalPreference notApplicable Unsigned32 setOrigin notApplicable { egp, igp, incomplete } (Note#2) setWeight notApplicable Interger32 (0..65535) setDampening notApplicable Interger32 (0..65535) setMetricType notApplicable Interger32 (0..65535) ======================================================================================== Note#1: Given a {route map, sequence number}, setCommunity will have at most one instance, i.e., all options and values will be aggregated into one dRouteMapClauseSubId. When 'additive' is chosen for dRouteMapClauseAddOption, the specified community list will be added to the existed community list. If 'communityNone' is chosen, the dRouteMapClauseElementValue should be a zeor-length string. When read dRouteMapClauseElementValue, the value 'additive' is never returned. Note#2: The element value needs choose the exact case-sensitive string to set the option. For example, for setOrigin, egp or igp or incomplete will be the valid options to select.")
dAccessListTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4), )
if mibBuilder.loadTexts: dAccessListTable.setStatus('current')
if mibBuilder.loadTexts: dAccessListTable.setDescription('This table contains name for IP access list.')
dAccessListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dAccessListName"), (0, "DLINKSW-IP-FILTER-MIB", "dAccessListAddrType"))
if mibBuilder.loadTexts: dAccessListEntry.setStatus('current')
if mibBuilder.loadTexts: dAccessListEntry.setDescription('An entry contains the information of IP access list.')
dAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: dAccessListName.setStatus('current')
if mibBuilder.loadTexts: dAccessListName.setDescription('The name of the IP access list.')
dAccessListAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1, 2), InetAddressType())
if mibBuilder.loadTexts: dAccessListAddrType.setStatus('current')
if mibBuilder.loadTexts: dAccessListAddrType.setDescription('This object indicates the address type of the access list.')
dAccessListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 4, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dAccessListRowStatus.setStatus('current')
if mibBuilder.loadTexts: dAccessListRowStatus.setDescription('This object indicates the status of this entry. Only createAndGo(4) and destroy(6) are supported.')
dAccessListRuleTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5), )
if mibBuilder.loadTexts: dAccessListRuleTable.setStatus('current')
if mibBuilder.loadTexts: dAccessListRuleTable.setDescription('This table contains rules for IP access list.')
dAccessListRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dAccessListName"), (0, "DLINKSW-IP-FILTER-MIB", "dAccessListAddrType"), (0, "DLINKSW-IP-FILTER-MIB", "dAccessListRuleMatchAction"), (0, "DLINKSW-IP-FILTER-MIB", "dAccessListRuleNetAddr"), (0, "DLINKSW-IP-FILTER-MIB", "dAccessListRulePfxLen"))
if mibBuilder.loadTexts: dAccessListRuleEntry.setStatus('current')
if mibBuilder.loadTexts: dAccessListRuleEntry.setDescription('An entry contains one rule of the IP access list.')
dAccessListRuleMatchAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2))))
if mibBuilder.loadTexts: dAccessListRuleMatchAction.setStatus('current')
if mibBuilder.loadTexts: dAccessListRuleMatchAction.setDescription('Indicates the action performed for this IP access list.')
dAccessListRuleNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 2), InetAddress())
if mibBuilder.loadTexts: dAccessListRuleNetAddr.setStatus('current')
if mibBuilder.loadTexts: dAccessListRuleNetAddr.setDescription('Indicates the network address.')
dAccessListRulePfxLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 3), Integer32())
if mibBuilder.loadTexts: dAccessListRulePfxLen.setStatus('current')
if mibBuilder.loadTexts: dAccessListRulePfxLen.setDescription('Indicates the prefix length of the network address.')
dAccessListRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 5, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dAccessListRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: dAccessListRuleRowStatus.setDescription('This object indicates the status of this entry. Only createAndGo(4) and destroy(6) are supported.')
dPrefixListTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6), )
if mibBuilder.loadTexts: dPrefixListTable.setStatus('current')
if mibBuilder.loadTexts: dPrefixListTable.setDescription('This table contains name for IP prefix list.')
dPrefixListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dPrefixListName"), (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListAddrType"))
if mibBuilder.loadTexts: dPrefixListEntry.setStatus('current')
if mibBuilder.loadTexts: dPrefixListEntry.setDescription('An entry contains the information of IP prefix list.')
dPrefixListName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: dPrefixListName.setStatus('current')
if mibBuilder.loadTexts: dPrefixListName.setDescription('The name of the IP prefix list.')
dPrefixListAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1, 2), InetAddressType())
if mibBuilder.loadTexts: dPrefixListAddrType.setStatus('current')
if mibBuilder.loadTexts: dPrefixListAddrType.setDescription('This object indicates the address type of the prefix.')
dPrefixListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 6, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListRowStatus.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRowStatus.setDescription('This object indicates the status of this entry. Only createAndGo(4) and destroy(6) are supported.')
dPrefixListRuleTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7), )
if mibBuilder.loadTexts: dPrefixListRuleTable.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleTable.setDescription('A table consists of a list of IP prefixes. The initial 2 index elements identify the prefix list that a prefix belongs to. ')
dPrefixListRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dPrefixListName"), (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListAddrType"), (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListRuleSeqNum"))
if mibBuilder.loadTexts: dPrefixListRuleEntry.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleEntry.setDescription('An entry contains the information of an IP prefix.')
dPrefixListRuleSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), )))
if mibBuilder.loadTexts: dPrefixListRuleSeqNum.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleSeqNum.setDescription('The checking sequence of the prefix within a prefix list. The lower the number is, the higher the precedence of the permit/deny rule. The special value of 0 means the sequence number will be automatically determined by the agent. ')
dPrefixListRuleAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListRuleAction.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleAction.setDescription('This object indicates whether to permit or deny the matched route entry.')
dPrefixListRuleNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListRuleNetAddr.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleNetAddr.setDescription('This object indicates the network address (prefix).')
dPrefixListRulePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 4), InetAddressPrefixLength()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListRulePrefixLen.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRulePrefixLen.setDescription('The length of network address (prefix).')
dPrefixListRuleGeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 128), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListRuleGeValue.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleGeValue.setDescription('The minimum prefix length of the route that can be matched. The special value of 0 indicates this object is not specified. ')
dPrefixListRuleLeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 128), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListRuleLeValue.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleLeValue.setDescription('The maximum prefix length of the route that can be matched. The special value of 0 indicates this object is not specified. ')
dPrefixListRuleHitCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dPrefixListRuleHitCount.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleHitCount.setDescription('Counter that the prefix list entry has been matched.')
dPrefixListRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 7, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleRowStatus.setDescription('This object indicates the status of this entry. Only createAndGo(4) and destroy(6) are supported.')
dPrefixListDescTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8), )
if mibBuilder.loadTexts: dPrefixListDescTable.setStatus('current')
if mibBuilder.loadTexts: dPrefixListDescTable.setDescription('A table consists of a list of descriptions for IP prefix lists.')
dPrefixListDescEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8, 1), ).setIndexNames((0, "DLINKSW-IP-FILTER-MIB", "dPrefixListName"), (0, "DLINKSW-IP-FILTER-MIB", "dPrefixListAddrType"))
if mibBuilder.loadTexts: dPrefixListDescEntry.setStatus('current')
if mibBuilder.loadTexts: dPrefixListDescEntry.setDescription('An entry contains the description of an IP prefix list.')
dPrefixListDescContent = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListDescContent.setStatus('current')
if mibBuilder.loadTexts: dPrefixListDescContent.setDescription('Specify the description for prefix list.')
dPrefixListDescRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 117, 1, 8, 1, 99), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dPrefixListDescRowStatus.setStatus('current')
if mibBuilder.loadTexts: dPrefixListDescRowStatus.setDescription('This object indicates the status of this entry. Only createAndGo(4) and destroy(6) are supported.')
dIPFilterMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1))
dIPFilterMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 2))
dIPFilterMIBFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 2, 1)).setObjects(("DLINKSW-IP-FILTER-MIB", "dRouteMapGroup"), ("DLINKSW-IP-FILTER-MIB", "dRouteMapSeqGroup"), ("DLINKSW-IP-FILTER-MIB", "dRouteMapClauseGroup"), ("DLINKSW-IP-FILTER-MIB", "dAccessListGroup"), ("DLINKSW-IP-FILTER-MIB", "dAccessListRuleGroup"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListGroup"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleGroup"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListDescGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dIPFilterMIBFullCompliance = dIPFilterMIBFullCompliance.setStatus('current')
if mibBuilder.loadTexts: dIPFilterMIBFullCompliance.setDescription('The compliance statement')
dRouteMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 1)).setObjects(("DLINKSW-IP-FILTER-MIB", "dRouteMapRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dRouteMapGroup = dRouteMapGroup.setStatus('current')
if mibBuilder.loadTexts: dRouteMapGroup.setDescription('These objects are used for managing/monitoring route map configurations.')
dRouteMapSeqGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 2)).setObjects(("DLINKSW-IP-FILTER-MIB", "dRouteMapSeqMatchAction"), ("DLINKSW-IP-FILTER-MIB", "dRouteMapSeqRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dRouteMapSeqGroup = dRouteMapSeqGroup.setStatus('current')
if mibBuilder.loadTexts: dRouteMapSeqGroup.setDescription('These objects are used for managing/monitoring route map sequence configurations.')
dRouteMapClauseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 3)).setObjects(("DLINKSW-IP-FILTER-MIB", "dRouteMapClauseAddOption"), ("DLINKSW-IP-FILTER-MIB", "dRouteMapClauseElementValue"), ("DLINKSW-IP-FILTER-MIB", "dRouteMapClauseRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dRouteMapClauseGroup = dRouteMapClauseGroup.setStatus('current')
if mibBuilder.loadTexts: dRouteMapClauseGroup.setDescription('These objects are used for managing/monitoring route map clauses.')
dAccessListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 4)).setObjects(("DLINKSW-IP-FILTER-MIB", "dAccessListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAccessListGroup = dAccessListGroup.setStatus('current')
if mibBuilder.loadTexts: dAccessListGroup.setDescription('These objects are used for managing/monitoring IP access list configuration.')
dAccessListRuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 5)).setObjects(("DLINKSW-IP-FILTER-MIB", "dAccessListRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dAccessListRuleGroup = dAccessListRuleGroup.setStatus('current')
if mibBuilder.loadTexts: dAccessListRuleGroup.setDescription('These objects are used for managing/monitoring IP access list rules configuration.')
dPrefixListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 6)).setObjects(("DLINKSW-IP-FILTER-MIB", "dPrefixListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dPrefixListGroup = dPrefixListGroup.setStatus('current')
if mibBuilder.loadTexts: dPrefixListGroup.setDescription('These objects are used for managing/monitoring route map clauses.')
dPrefixListRuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 7)).setObjects(("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleAction"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleNetAddr"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListRulePrefixLen"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleGeValue"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleLeValue"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleHitCount"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dPrefixListRuleGroup = dPrefixListRuleGroup.setStatus('current')
if mibBuilder.loadTexts: dPrefixListRuleGroup.setDescription('These objects are used for managing/monitoring IP access list configuration.')
dPrefixListDescGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 12, 117, 2, 1, 8)).setObjects(("DLINKSW-IP-FILTER-MIB", "dPrefixListDescContent"), ("DLINKSW-IP-FILTER-MIB", "dPrefixListDescRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dPrefixListDescGroup = dPrefixListDescGroup.setStatus('current')
if mibBuilder.loadTexts: dPrefixListDescGroup.setDescription('These objects are used for managing/monitoring IP access list rules configuration.')
mibBuilder.exportSymbols("DLINKSW-IP-FILTER-MIB", dAccessListRuleEntry=dAccessListRuleEntry, dAccessListGroup=dAccessListGroup, dRouteMapSeqMatchAction=dRouteMapSeqMatchAction, dRouteMapSeqGroup=dRouteMapSeqGroup, dAccessListRuleNetAddr=dAccessListRuleNetAddr, dRouteMapEntry=dRouteMapEntry, dRouteMapSeqRowStatus=dRouteMapSeqRowStatus, dAccessListRuleTable=dAccessListRuleTable, dIPFilterNotifications=dIPFilterNotifications, dAccessListAddrType=dAccessListAddrType, dAccessListRuleGroup=dAccessListRuleGroup, dPrefixListGroup=dPrefixListGroup, dIPFilterMIBCompliances=dIPFilterMIBCompliances, dAccessListName=dAccessListName, dIPFilterObjects=dIPFilterObjects, dPrefixListTable=dPrefixListTable, dPrefixListAddrType=dPrefixListAddrType, dIPFilterMIBGroups=dIPFilterMIBGroups, dPrefixListDescEntry=dPrefixListDescEntry, dRouteMapGroup=dRouteMapGroup, dAccessListRulePfxLen=dAccessListRulePfxLen, dlinkSwIPFilterMIB=dlinkSwIPFilterMIB, dRouteMapClauseTable=dRouteMapClauseTable, dAccessListRuleRowStatus=dAccessListRuleRowStatus, dRouteMapName=dRouteMapName, dRouteMapClauseSubId=dRouteMapClauseSubId, dRouteMapClauseTypeId=dRouteMapClauseTypeId, dPrefixListRulePrefixLen=dPrefixListRulePrefixLen, dRouteMapRowStatus=dRouteMapRowStatus, dRouteMapClauseRowStatus=dRouteMapClauseRowStatus, dRouteMapClauseGroup=dRouteMapClauseGroup, dPrefixListRuleTable=dPrefixListRuleTable, dRouteMapClauseElementValue=dRouteMapClauseElementValue, dPrefixListRuleNetAddr=dPrefixListRuleNetAddr, dPrefixListRuleGeValue=dPrefixListRuleGeValue, dPrefixListRowStatus=dPrefixListRowStatus, dIPFilterConform=dIPFilterConform, dPrefixListDescTable=dPrefixListDescTable, dPrefixListDescRowStatus=dPrefixListDescRowStatus, dAccessListTable=dAccessListTable, dAccessListRowStatus=dAccessListRowStatus, dAccessListEntry=dAccessListEntry, dPrefixListName=dPrefixListName, dPrefixListRuleSeqNum=dPrefixListRuleSeqNum, dRouteMapSeqTable=dRouteMapSeqTable, dPrefixListRuleGroup=dPrefixListRuleGroup, dPrefixListRuleAction=dPrefixListRuleAction, dRouteMapTable=dRouteMapTable, dRouteMapClauseEntry=dRouteMapClauseEntry, dPrefixListRuleHitCount=dPrefixListRuleHitCount, dPrefixListRuleLeValue=dPrefixListRuleLeValue, dPrefixListRuleRowStatus=dPrefixListRuleRowStatus, dAccessListRuleMatchAction=dAccessListRuleMatchAction, dRouteMapClauseAddOption=dRouteMapClauseAddOption, dIPFilterMIBFullCompliance=dIPFilterMIBFullCompliance, dPrefixListEntry=dPrefixListEntry, dPrefixListDescGroup=dPrefixListDescGroup, dRouteMapSeqNum=dRouteMapSeqNum, dPrefixListRuleEntry=dPrefixListRuleEntry, dPrefixListDescContent=dPrefixListDescContent, dRouteMapSeqEntry=dRouteMapSeqEntry, PYSNMP_MODULE_ID=dlinkSwIPFilterMIB)