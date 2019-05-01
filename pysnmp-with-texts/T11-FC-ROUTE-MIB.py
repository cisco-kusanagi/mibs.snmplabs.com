#
# PySNMP MIB module T11-FC-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/T11-FC-ROUTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:14:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
FcDomainIdOrZero, fcmSwitchIndex, fcmInstanceIndex, FcAddressIdOrZero = mibBuilder.importSymbols("FC-MGMT-MIB", "FcDomainIdOrZero", "fcmSwitchIndex", "fcmInstanceIndex", "FcAddressIdOrZero")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, Integer32, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, IpAddress, Counter64, Gauge32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Integer32", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "IpAddress", "Counter64", "Gauge32", "Unsigned32", "iso")
TextualConvention, TimeStamp, RowStatus, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "RowStatus", "DisplayString", "StorageType")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcRouteMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 144))
t11FcRouteMIB.setRevisions(('2006-08-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: t11FcRouteMIB.setRevisionsDescriptions(('Initial version of this MIB module, published as RFC4625.',))
if mibBuilder.loadTexts: t11FcRouteMIB.setLastUpdated('200608140000Z')
if mibBuilder.loadTexts: t11FcRouteMIB.setOrganization('T11')
if mibBuilder.loadTexts: t11FcRouteMIB.setContactInfo(' Claudio DeSanti Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134 USA EMail: cds@cisco.com Keith McCloghrie Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA USA 95134 Email: kzm@cisco.com')
if mibBuilder.loadTexts: t11FcRouteMIB.setDescription('The MIB module for configuring and displaying Fibre Channel Route Information. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4625; see the RFC itself for full legal notices.')
t11FcRouteNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 144, 0))
t11FcRouteObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 144, 1))
t11FcRouteConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 144, 2))
t11FcRouteFabricTable = MibTable((1, 3, 6, 1, 2, 1, 144, 1, 1), )
if mibBuilder.loadTexts: t11FcRouteFabricTable.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteFabricTable.setDescription('The table containing Fibre Channel Routing information that is specific to a Fabric.')
t11FcRouteFabricEntry = MibTableRow((1, 3, 6, 1, 2, 1, 144, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteFabricIndex"))
if mibBuilder.loadTexts: t11FcRouteFabricEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteFabricEntry.setDescription('Each entry contains routing information specific to a particular Fabric on a particular switch (identified by values of fcmInstanceIndex and fcmSwitchIndex).')
t11FcRouteFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: t11FcRouteFabricIndex.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteFabricIndex.setDescription('A unique index value that uniquely identifies a particular Fabric. In a Fabric conformant to FC-SW-3, only a single Fabric can operate within a physical infrastructure, and thus the value of this Fabric Index will always be 1. In a Fabric conformant to FC-SW-4, multiple Virtual Fabrics can operate within one (or more) physical infrastructures. In such a case, index value is used to uniquely identify a particular Fabric within a physical infrastructure.')
t11FcRouteFabricLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FcRouteFabricLastChange.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteFabricLastChange.setDescription('The value of sysUpTime at the most recent time when any corresponding row in the t11FcRouteTable was created, modified, or deleted. A corresponding row in the t11FcRouteTable is for the same management instance, the same switch, and same Fabric as the row in this table. If no change has occurred since the last restart of the management system, then the value of this object is 0.')
t11FcRouteTable = MibTable((1, 3, 6, 1, 2, 1, 144, 1, 2), )
if mibBuilder.loadTexts: t11FcRouteTable.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteTable.setDescription("The Fibre Channel Routing tables for the locally managed switches. This table lists all the routes that are configured in and/or computed by any local switch for any Fabric. Such routes are used by a switch to forward frames (of user data) on a Fabric. The conceptual process is based on extracting the Destination Fibre Channel Address Identifier (D_ID) out of a received frame (of user data) and comparing it to each entry of this table that is applicable to the given switch and Fabric. Such comparison consists of first performing a logical-AND of the extracted D_ID with a mask (the value of t11FcRouteDestMask) and second comparing the result of that 'AND' operation to the value of t11FcRouteDestAddrId. A similar comparison is made of the Source Fibre Channel Address Identifier (S_ID) of a frame against the t11FcRouteSrcAddrId and t11FcRouteSrcMask values of an entry. If an entry's value of t11FcRouteInInterface is non-zero, then a further comparison determines if the frame was received on the appropriate interface. If all of these comparisons for a particular entry are successful, then that entry represents a potential route for forwarding the received frame. For entries configured by a user, t11FcRouteProto has the value 'netmgmt'; only entries of this type can be deleted by the user.")
t11FcRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 144, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteFabricIndex"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteDestAddrId"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteDestMask"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteSrcAddrId"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteSrcMask"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteInInterface"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteProto"), (0, "T11-FC-ROUTE-MIB", "t11FcRouteOutInterface"))
if mibBuilder.loadTexts: t11FcRouteEntry.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteEntry.setDescription('Each entry contains a route to a particular destination, possibly from a particular subset of source addresses, on a particular Fabric via a particular output interface and learned in a particular manner.')
t11FcRouteDestAddrId = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 1), FcAddressIdOrZero().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3))
if mibBuilder.loadTexts: t11FcRouteDestAddrId.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteDestAddrId.setDescription('The destination Fibre Channel Address Identifier of this route. A zero-length string for this field is not allowed.')
t11FcRouteDestMask = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 2), FcAddressIdOrZero())
if mibBuilder.loadTexts: t11FcRouteDestMask.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteDestMask.setDescription("The mask to be logical-ANDed with a destination Fibre Channel Address Identifier before it is compared to the value in the t11FcRouteDestAddrId field. Allowed values are 255.255.255, 255.255.0, or 255.0.0. FSPF's definition generates routes to a Domain_ID, so the mask for all FSPF-generated routes is 255.0.0. The zero-length value has the same meaning as 0.0.0.")
t11FcRouteSrcAddrId = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 3), FcAddressIdOrZero())
if mibBuilder.loadTexts: t11FcRouteSrcAddrId.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteSrcAddrId.setDescription('The source Fibre Channel Address Identifier of this route. Note that if this object and the corresponding instance of t11FcRouteSrcMask both have a value of 0.0.0, then this route matches all source addresses. The zero-length value has the same meaning as 0.0.0.')
t11FcRouteSrcMask = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 4), FcAddressIdOrZero())
if mibBuilder.loadTexts: t11FcRouteSrcMask.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteSrcMask.setDescription('The mask to be logical-ANDed with a source Fibre Channel Address Identifier before it is compared to the value in the t11FcRouteSrcAddrId field. Allowed values are 255.255.255, 255.255.0, 255.0.0, or 0.0.0. The zero-length value has the same meaning as 0.0.0.')
t11FcRouteInInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 5), InterfaceIndexOrZero())
if mibBuilder.loadTexts: t11FcRouteInInterface.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteInInterface.setDescription('If the value of this object is non-zero, it is the value of ifIndex that identifies the local Fibre Channel interface through which a frame must have been received in order to match with this entry. If the value of this object is zero, the matching does not require that the frame be received on any specific interface.')
t11FcRouteProto = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("fspf", 4))))
if mibBuilder.loadTexts: t11FcRouteProto.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteProto.setDescription('The mechanism via which this route was learned: other(1) - not specified local(2) - local interface netmgmt(3)- static route fspf(4) - Fibre Shortest Path First ')
t11FcRouteOutInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 7), InterfaceIndex())
if mibBuilder.loadTexts: t11FcRouteOutInterface.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteOutInterface.setDescription('The value of ifIndex that identifies the local Fibre Channel interface through which the next hop of this route is to be reached.')
t11FcRouteDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 8), FcDomainIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FcRouteDomainId.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteDomainId.setDescription("The domain_ID of next hop switch. This object can have a value of zero if the value of t11FcRouteProto is 'local'.")
t11FcRouteMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FcRouteMetric.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteMetric.setDescription('The routing metric for this route. The use of this object is dependent on t11FcRouteProto.')
t11FcRouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2))).clone('local')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FcRouteType.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteType.setDescription('The type of route. local(1) - a route for which the next Fibre Channel port is the final destination; remote(2) - a route for which the next Fibre Channel port is not the final destination.')
t11FcRouteIfDown = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("remove", 1), ("retain", 2))).clone('retain')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FcRouteIfDown.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteIfDown.setDescription("The value of this object indicates what happens to this route when the output interface (given by the corresponding value of t11FcRouteOutInterface) is operationally 'down'. If this object's value is 'retain', the route is to be retained in this table. If this object's value is 'remove', the route is to be removed from this table.")
t11FcRouteStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 12), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FcRouteStorageType.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteStorageType.setDescription("The storage type for this conceptual row. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row.")
t11FcRouteRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 144, 1, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FcRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteRowStatus.setDescription("The status of this conceptual row. The only rows that can be deleted by setting this object to 'destroy' are those for which t11FcRouteProto has the value 'netmgmt'.")
t11FcRouteCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 144, 2, 1))
t11FcRouteGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 144, 2, 2))
t11FcRouteCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 144, 2, 1, 1)).setObjects(("T11-FC-ROUTE-MIB", "t11FcRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcRouteCompliance = t11FcRouteCompliance.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteCompliance.setDescription("The compliance statement for entities that implement the T11-FC-ROUTE-MIB. -- -- Note: The next four OBJECT clauses are for auxiliary objects, and the -- SMIv2 does not permit inclusion of objects that are not accessible -- in an OBJECT clause (see Sections 3.1 & 5.4.3 in STD 58, RFC 2580). -- Thus, these four clauses cannot be included below in the normal -- location for OBJECT clauses. -- -- OBJECT t11FcRouteSrcAddrId -- SYNTAX FcAddressIdOrZero (SIZE (0)) -- DESCRIPTION -- 'Support is not required for routes that -- match only a subset of possible source -- addresses.' -- -- OBJECT t11FcRouteSrcMask -- SYNTAX FcAddressIdOrZero (SIZE (0)) -- DESCRIPTION -- 'Support is not required for routes that -- match only a subset of possible source -- addresses.' -- -- OBJECT t11FcRouteDestMask -- DESCRIPTION -- 'Support is mandatory only for FSPF-generated -- routes. Since FSPF's definition generates -- routes to a Domain_ID, the mask for all -- FSPF-generated routes is 255.0.0. Thus, -- support is only required for 255.0.0.' -- -- OBJECT t11FcRouteInInterface -- SYNTAX InterfaceIndexOrZero (0) -- DESCRIPTION -- 'Support for routes specific to particular -- source interfaces is not required.' ")
t11FcRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 144, 2, 2, 1)).setObjects(("T11-FC-ROUTE-MIB", "t11FcRouteFabricLastChange"), ("T11-FC-ROUTE-MIB", "t11FcRouteDomainId"), ("T11-FC-ROUTE-MIB", "t11FcRouteMetric"), ("T11-FC-ROUTE-MIB", "t11FcRouteType"), ("T11-FC-ROUTE-MIB", "t11FcRouteIfDown"), ("T11-FC-ROUTE-MIB", "t11FcRouteStorageType"), ("T11-FC-ROUTE-MIB", "t11FcRouteRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11FcRouteGroup = t11FcRouteGroup.setStatus('current')
if mibBuilder.loadTexts: t11FcRouteGroup.setDescription('A collection of objects for displaying and configuring routes.')
mibBuilder.exportSymbols("T11-FC-ROUTE-MIB", t11FcRouteInInterface=t11FcRouteInInterface, t11FcRouteMetric=t11FcRouteMetric, t11FcRouteFabricEntry=t11FcRouteFabricEntry, t11FcRouteGroups=t11FcRouteGroups, t11FcRouteType=t11FcRouteType, t11FcRouteStorageType=t11FcRouteStorageType, t11FcRouteObjects=t11FcRouteObjects, t11FcRouteDestMask=t11FcRouteDestMask, t11FcRouteCompliance=t11FcRouteCompliance, t11FcRouteProto=t11FcRouteProto, t11FcRouteFabricLastChange=t11FcRouteFabricLastChange, t11FcRouteFabricIndex=t11FcRouteFabricIndex, t11FcRouteTable=t11FcRouteTable, t11FcRouteFabricTable=t11FcRouteFabricTable, t11FcRouteSrcAddrId=t11FcRouteSrcAddrId, t11FcRouteEntry=t11FcRouteEntry, t11FcRouteNotifications=t11FcRouteNotifications, t11FcRouteRowStatus=t11FcRouteRowStatus, t11FcRouteDestAddrId=t11FcRouteDestAddrId, t11FcRouteGroup=t11FcRouteGroup, t11FcRouteConformance=t11FcRouteConformance, t11FcRouteOutInterface=t11FcRouteOutInterface, t11FcRouteMIB=t11FcRouteMIB, t11FcRouteSrcMask=t11FcRouteSrcMask, t11FcRouteDomainId=t11FcRouteDomainId, t11FcRouteIfDown=t11FcRouteIfDown, PYSNMP_MODULE_ID=t11FcRouteMIB, t11FcRouteCompliances=t11FcRouteCompliances)