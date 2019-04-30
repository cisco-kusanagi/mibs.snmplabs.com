#
# PySNMP MIB module COMMUNITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COMMUNITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, iso, TimeTicks, ObjectIdentity, Counter64, ModuleIdentity, NotificationType, Counter32, enterprises, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "iso", "TimeTicks", "ObjectIdentity", "Counter64", "ModuleIdentity", "NotificationType", "Counter32", "enterprises", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
commsDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1))
community = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 1, 52))
communityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 1, 52, 2), )
if mibBuilder.loadTexts: communityTable.setStatus('mandatory')
communityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1), ).setIndexNames((0, "COMMUNITY-MIB", "communityIndex"))
if mibBuilder.loadTexts: communityEntry.setStatus('mandatory')
communityName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityName.setStatus('mandatory')
communityTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityTrap.setStatus('mandatory')
communityIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: communityIPAddr.setStatus('mandatory')
communityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 1, 52, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: communityIndex.setStatus('mandatory')
mibBuilder.exportSymbols("COMMUNITY-MIB", cabletron=cabletron, communityTable=communityTable, communityIPAddr=communityIPAddr, communityEntry=communityEntry, communityIndex=communityIndex, communityName=communityName, community=community, communityTrap=communityTrap, commsDevice=commsDevice)
