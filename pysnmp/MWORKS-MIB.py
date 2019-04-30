#
# PySNMP MIB module MWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MWORKS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, NotificationType, Counter64, Counter32, Unsigned32, Bits, IpAddress, TimeTicks, enterprises, Gauge32, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Counter64", "Counter32", "Unsigned32", "Bits", "IpAddress", "TimeTicks", "enterprises", "Gauge32", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tecElite = MibIdentifier((1, 3, 6, 1, 4, 1, 217))
meterWorks = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 16))
mw501 = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 16, 1))
mwMem = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 16, 1, 1))
mwHeap = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 16, 1, 2))
mwMemCeiling = MibScalar((1, 3, 6, 1, 4, 1, 217, 16, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwMemCeiling.setStatus('mandatory')
mwMemUsed = MibScalar((1, 3, 6, 1, 4, 1, 217, 16, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwMemUsed.setStatus('mandatory')
mwHeapTotal = MibScalar((1, 3, 6, 1, 4, 1, 217, 16, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwHeapTotal.setStatus('mandatory')
mwHeapUsed = MibScalar((1, 3, 6, 1, 4, 1, 217, 16, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwHeapUsed.setStatus('mandatory')
mibBuilder.exportSymbols("MWORKS-MIB", meterWorks=meterWorks, mw501=mw501, tecElite=tecElite, mwMemCeiling=mwMemCeiling, mwHeapUsed=mwHeapUsed, mwHeap=mwHeap, mwHeapTotal=mwHeapTotal, mwMem=mwMem, mwMemUsed=mwMemUsed)
