#
# PySNMP MIB module BSUMSUBNETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSUMSUBNETS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
aniBsuWirelessPort, = mibBuilder.importSymbols("BSUWIRELESSIF-MIB", "aniBsuWirelessPort")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ModuleIdentity, Unsigned32, IpAddress, Integer32, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ModuleIdentity", "Unsigned32", "IpAddress", "Integer32", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniBsuMultSubnets = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 6))
if mibBuilder.loadTexts: aniBsuMultSubnets.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniBsuMultSubnets.setOrganization('Aperto Networks')
if mibBuilder.loadTexts: aniBsuMultSubnets.setContactInfo(' Postal: Aperto Networks Inc 1637 S Main Street Milpitas, California 95035 Tel: +1 408 719 9977 ')
if mibBuilder.loadTexts: aniBsuMultSubnets.setDescription('This group gives the BSU Multiple Subnets information. The aniBsuSubnetConfTable is used to view and configure subnets per wireless port. There can be upto 1024 <Ip Address/Subnet Mask> pairs. For a given WSS port, there can be multiple and different subnets. This means that each subnet specified by an <Ip Address masked by the Subnet Mask> has to be distinct. Atleast one Ip Address and Subnet Mask has to be specified. In addition to the subnet being distinct, each IP Address must be unique too. If clustering is disabled, then Multiple Subnets on one WSS port should not clash with Multiple Subnets on any other WSS port. Clustering and multiple subnets can exists simultaneously as long as they are not on the same WSS. If clustering is enabled but not all WSS are clustered, then those that are not part of the cluster can have multiple subnets. Eg. If WSS1 and WSS2 are clustered, but WSS3 and WSS4 are not, then WSS3 and WSS4 can have multiple subnets. To add a new subnet to the table, first set the aniBsuSubnetConfAddr. Next send an SNMP set request on aniBsuSubnetConfMask. Currently, deletion and modification of entries is not supported. When the BSU is in Bridge mode, this multiple subnets table is not valid and will not be displayed. ')
aniBsuSubnetConfTable = MibTable((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1), )
if mibBuilder.loadTexts: aniBsuSubnetConfTable.setStatus('current')
if mibBuilder.loadTexts: aniBsuSubnetConfTable.setDescription('This table contains the Multiple Subnets information per wireless port. ')
aniBsuSubnetConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1), ).setIndexNames((0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"), (0, "BSUMSUBNETS-MIB", "aniBsuSubnetConfAddr"))
if mibBuilder.loadTexts: aniBsuSubnetConfEntry.setStatus('current')
if mibBuilder.loadTexts: aniBsuSubnetConfEntry.setDescription('An entry in the aniBsuSubnetConfTable. ')
aniBsuSubnetConfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aniBsuSubnetConfAddr.setStatus('current')
if mibBuilder.loadTexts: aniBsuSubnetConfAddr.setDescription('The IP Address of the configured Subnet. ')
aniBsuSubnetConfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aniBsuSubnetConfMask.setStatus('current')
if mibBuilder.loadTexts: aniBsuSubnetConfMask.setDescription('The Subnet Mask. ')
mibBuilder.exportSymbols("BSUMSUBNETS-MIB", PYSNMP_MODULE_ID=aniBsuMultSubnets, aniBsuMultSubnets=aniBsuMultSubnets, aniBsuSubnetConfMask=aniBsuSubnetConfMask, aniBsuSubnetConfAddr=aniBsuSubnetConfAddr, aniBsuSubnetConfTable=aniBsuSubnetConfTable, aniBsuSubnetConfEntry=aniBsuSubnetConfEntry)
