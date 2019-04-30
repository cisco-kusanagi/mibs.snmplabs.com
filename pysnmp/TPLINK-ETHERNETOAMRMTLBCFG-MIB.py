#
# PySNMP MIB module TPLINK-ETHERNETOAMRMTLBCFG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-ETHERNETOAMRMTLBCFG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, iso, TimeTicks, Integer32, Counter32, NotificationType, Gauge32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "iso", "TimeTicks", "Integer32", "Counter32", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ethernetOamRmtLbConfig, = mibBuilder.importSymbols("TPLINK-ETHERNETOAM-MIB", "ethernetOamRmtLbConfig")
ethernetOamRmtLbCfgTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1), )
if mibBuilder.loadTexts: ethernetOamRmtLbCfgTable.setStatus('current')
ethernetOamRmtLbCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ethernetOamRmtLbCfgEntry.setStatus('current')
ethernetOamRmtLbCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgPort.setStatus('current')
ethernetOamRmtLbCfgReceivedRemoteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ignore", 0), ("process", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgReceivedRemoteLoopback.setStatus('current')
ethernetOamRmtLbCfgRemoteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("stop", 0), ("start", 1), ("unchanged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgRemoteLoopback.setStatus('current')
ethernetOamRmtLbCfgLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethernetOamRmtLbCfgLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-ETHERNETOAMRMTLBCFG-MIB", ethernetOamRmtLbCfgTable=ethernetOamRmtLbCfgTable, ethernetOamRmtLbCfgEntry=ethernetOamRmtLbCfgEntry, ethernetOamRmtLbCfgReceivedRemoteLoopback=ethernetOamRmtLbCfgReceivedRemoteLoopback, ethernetOamRmtLbCfgRemoteLoopback=ethernetOamRmtLbCfgRemoteLoopback, ethernetOamRmtLbCfgLAG=ethernetOamRmtLbCfgLAG, ethernetOamRmtLbCfgPort=ethernetOamRmtLbCfgPort)
