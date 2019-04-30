#
# PySNMP MIB module RADLAN-SNA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-SNA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:40:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, ObjectIdentity, IpAddress, Counter64, TimeTicks, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "ObjectIdentity", "IpAddress", "Counter64", "TimeTicks", "Bits", "Gauge32")
DisplayString, TextualConvention, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TestAndIncr")
rlSna = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 229))
rlSna.setRevisions(('2015-05-12 00:00',))
if mibBuilder.loadTexts: rlSna.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlSna.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlSnaNextFreeSessionId = MibScalar((1, 3, 6, 1, 4, 1, 89, 229, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnaNextFreeSessionId.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SNA-MIB", PYSNMP_MODULE_ID=rlSna, rlSnaNextFreeSessionId=rlSnaNextFreeSessionId, rlSna=rlSna)
