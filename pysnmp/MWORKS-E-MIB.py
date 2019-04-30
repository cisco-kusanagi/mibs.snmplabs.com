#
# PySNMP MIB module MWORKS-E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MWORKS-E-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, enterprises, Bits, Unsigned32, iso, Counter64, ModuleIdentity, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "enterprises", "Bits", "Unsigned32", "iso", "Counter64", "ModuleIdentity", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tecElite = MibIdentifier((1, 3, 6, 1, 4, 1, 217))
mworkse = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 17))
am501 = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 17, 1))
amMem = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 17, 1, 1))
amHeap = MibIdentifier((1, 3, 6, 1, 4, 1, 217, 17, 1, 2))
amMemCeiling = MibScalar((1, 3, 6, 1, 4, 1, 217, 17, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: amMemCeiling.setStatus('mandatory')
amMemUsed = MibScalar((1, 3, 6, 1, 4, 1, 217, 17, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: amMemUsed.setStatus('mandatory')
amHeapTotal = MibScalar((1, 3, 6, 1, 4, 1, 217, 17, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: amHeapTotal.setStatus('mandatory')
amHeapUsed = MibScalar((1, 3, 6, 1, 4, 1, 217, 17, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: amHeapUsed.setStatus('mandatory')
mibBuilder.exportSymbols("MWORKS-E-MIB", amHeapTotal=amHeapTotal, mworkse=mworkse, amHeapUsed=amHeapUsed, am501=am501, amMem=amMem, amMemCeiling=amMemCeiling, amMemUsed=amMemUsed, tecElite=tecElite, amHeap=amHeap)
