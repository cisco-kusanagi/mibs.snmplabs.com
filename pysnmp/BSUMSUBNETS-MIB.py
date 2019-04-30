#
# PySNMP MIB module BSUMSUBNETS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BSUMSUBNETS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
aniBsuWirelessPort, = mibBuilder.importSymbols("BSUWIRELESSIF-MIB", "aniBsuWirelessPort")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Unsigned32, MibIdentifier, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ModuleIdentity, Integer32, IpAddress, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "IpAddress", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniBsuMultSubnets = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 6))
if mibBuilder.loadTexts: aniBsuMultSubnets.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniBsuMultSubnets.setOrganization('Aperto Networks')
aniBsuSubnetConfTable = MibTable((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1), )
if mibBuilder.loadTexts: aniBsuSubnetConfTable.setStatus('current')
aniBsuSubnetConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1), ).setIndexNames((0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"), (0, "BSUMSUBNETS-MIB", "aniBsuSubnetConfAddr"))
if mibBuilder.loadTexts: aniBsuSubnetConfEntry.setStatus('current')
aniBsuSubnetConfAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aniBsuSubnetConfAddr.setStatus('current')
aniBsuSubnetConfMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4325, 3, 6, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aniBsuSubnetConfMask.setStatus('current')
mibBuilder.exportSymbols("BSUMSUBNETS-MIB", aniBsuSubnetConfTable=aniBsuSubnetConfTable, aniBsuSubnetConfEntry=aniBsuSubnetConfEntry, aniBsuSubnetConfMask=aniBsuSubnetConfMask, aniBsuSubnetConfAddr=aniBsuSubnetConfAddr, aniBsuMultSubnets=aniBsuMultSubnets, PYSNMP_MODULE_ID=aniBsuMultSubnets)
