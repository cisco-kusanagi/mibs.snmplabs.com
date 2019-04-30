#
# PySNMP MIB module MICOMETHER (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICOMETHER
# Produced by pysmi-0.3.4 at Mon Apr 29 20:02:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
micom_oscar, = mibBuilder.importSymbols("MICOM-OSCAR-MIB", "micom-oscar")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Integer32, Bits, Counter64, TimeTicks, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mcmEth = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 10))
mcmEthCntr = MibIdentifier((1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1))
mcmEthCntrZeroTable = MibTable((1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1), )
if mibBuilder.loadTexts: mcmEthCntrZeroTable.setStatus('obsolete')
mcmEthCntrZeroEntry = MibTableRow((1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1), ).setIndexNames((0, "MICOMETHER", "mcmEthCntrZeroPort"))
if mibBuilder.loadTexts: mcmEthCntrZeroEntry.setStatus('obsolete')
mcmEthCntrZeroPort = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mcmEthCntrZeroPort.setStatus('obsolete')
mcmEthStatsGrpCounterZero = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("other", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mcmEthStatsGrpCounterZero.setStatus('obsolete')
mcmEthCollStatsGrpCounterZero = MibTableColumn((1, 3, 6, 1, 4, 1, 335, 1, 4, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("other", 2)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mcmEthCollStatsGrpCounterZero.setStatus('obsolete')
mibBuilder.exportSymbols("MICOMETHER", mcmEthCntrZeroEntry=mcmEthCntrZeroEntry, mcmEthCollStatsGrpCounterZero=mcmEthCollStatsGrpCounterZero, mcmEthCntrZeroTable=mcmEthCntrZeroTable, mcmEth=mcmEth, mcmEthCntr=mcmEthCntr, mcmEthStatsGrpCounterZero=mcmEthStatsGrpCounterZero, mcmEthCntrZeroPort=mcmEthCntrZeroPort)
