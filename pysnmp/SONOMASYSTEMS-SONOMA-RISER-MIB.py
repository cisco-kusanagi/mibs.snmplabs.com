#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-RISER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-RISER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, IpAddress, NotificationType, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Integer32, ObjectIdentity, Gauge32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "IpAddress", "NotificationType", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Integer32", "ObjectIdentity", "Gauge32", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonomaSeries, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaSeries")
sonomaRiser = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 12))
riserFanTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1), )
if mibBuilder.loadTexts: riserFanTable.setStatus('mandatory')
riserFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-RISER-MIB", "riserFanIndex"))
if mibBuilder.loadTexts: riserFanEntry.setStatus('mandatory')
riserFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: riserFanIndex.setStatus('mandatory')
riserFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: riserFanStatus.setStatus('mandatory')
thermalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 12, 2))
riserTemperatureC = MibScalar((1, 3, 6, 1, 4, 1, 2926, 25, 12, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: riserTemperatureC.setStatus('mandatory')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-RISER-MIB", thermalGroup=thermalGroup, riserFanStatus=riserFanStatus, riserFanTable=riserFanTable, sonomaRiser=sonomaRiser, riserTemperatureC=riserTemperatureC, riserFanIndex=riserFanIndex, riserFanEntry=riserFanEntry)
