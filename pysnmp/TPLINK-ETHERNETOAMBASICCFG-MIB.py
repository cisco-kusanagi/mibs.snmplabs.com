#
# PySNMP MIB module TPLINK-ETHERNETOAMBASICCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAMBASICCFG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Integer32, Gauge32, IpAddress, Counter32, ObjectIdentity, Bits, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "IpAddress", "Counter32", "ObjectIdentity", "Bits", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ethernetOamBasicConfig, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamBasicConfig")
ethernetOamBasicCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1), )
if mibBuilder.loadTexts: ethernetOamBasicCfgTable.setStatus('current')
ethernetOamBasicCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamBasicCfgEntry.setStatus('current')
ethernetOamBasicCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamBasicCfgPort.setStatus('current')
ethernetOamBasicCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("passive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamBasicCfgMode.setStatus('current')
ethernetOamBasicCfgState = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamBasicCfgState.setStatus('current')
ethernetOamBasicCfgLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamBasicCfgLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMBASICCFG-MIB", ethernetOamBasicCfgTable=ethernetOamBasicCfgTable, ethernetOamBasicCfgState=ethernetOamBasicCfgState, ethernetOamBasicCfgLAG=ethernetOamBasicCfgLAG, ethernetOamBasicCfgPort=ethernetOamBasicCfgPort, ethernetOamBasicCfgEntry=ethernetOamBasicCfgEntry, ethernetOamBasicCfgMode=ethernetOamBasicCfgMode)
