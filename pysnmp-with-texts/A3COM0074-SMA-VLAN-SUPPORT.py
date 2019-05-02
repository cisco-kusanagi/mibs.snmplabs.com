#
# PySNMP MIB module A3COM0074-SMA-VLAN-SUPPORT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0074-SMA-VLAN-SUPPORT
# Produced by pysmi-0.3.4 at Wed May  1 11:09:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
smaVlanSupport, = mibBuilder.importSymbols("A3COM0004-GENERIC", "smaVlanSupport")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
a3ComVlanIfIndex, = mibBuilder.importSymbols("GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanIfIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Integer32, ObjectIdentity, Counter64, IpAddress, MibIdentifier, iso, ModuleIdentity, Unsigned32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Integer32", "ObjectIdentity", "Counter64", "IpAddress", "MibIdentifier", "iso", "ModuleIdentity", "Unsigned32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3ComVlanPrivateIfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 35, 1), )
if mibBuilder.loadTexts: a3ComVlanPrivateIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanPrivateIfTable.setDescription('Private VLAN information table for internal agent operations.')
a3ComVlanPrivateIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 35, 1, 1), ).setIndexNames((0, "GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanIfIndex"))
if mibBuilder.loadTexts: a3ComVlanPrivateIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanPrivateIfEntry.setDescription('An individual VLAN interface entry. When an NMS wishes to create a new entry in this table, it must obtain a non-zero index from the a3ComNextAvailableVirtIfIndex object. Row creation in this table will fail if the chosen index value does not match the current value returned from the a3ComNextAvailableVirtIfIndex object.')
a3ComVlanCreateType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 35, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("automatic", 1), ("dynamic", 2), ("manual", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComVlanCreateType.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanCreateType.setDescription('The reason this Vlan has been created. The possible values are: automatic (1) - This VLAN was created on this unit due to replication across a stack of units. dynamic (2) - VLAN created internally by some automatic mechanism, for example GVRP. manual (3) - VLAN created by some external management application. NOTE - This MIB object may only be set by the agent. It is illegal and serves no purpose for this object to be set for some other application.')
a3ComVlanMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 35, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComVlanMembers.setStatus('mandatory')
if mibBuilder.loadTexts: a3ComVlanMembers.setDescription('Total number of members of this VLAN across the entire stack. If the value of this MIB object is zero then the VLAN is not currently in use on any device in the stack.')
mibBuilder.exportSymbols("A3COM0074-SMA-VLAN-SUPPORT", a3ComVlanPrivateIfEntry=a3ComVlanPrivateIfEntry, a3ComVlanCreateType=a3ComVlanCreateType, a3ComVlanMembers=a3ComVlanMembers, a3ComVlanPrivateIfTable=a3ComVlanPrivateIfTable)
