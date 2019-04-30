#
# PySNMP MIB module RADLAN-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-JUMBOFRAMES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:38:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, IpAddress, Unsigned32, Bits, Counter64, MibIdentifier, ModuleIdentity, iso, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "IpAddress", "Unsigned32", "Bits", "Counter64", "MibIdentifier", "ModuleIdentity", "iso", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
mibBuilder.exportSymbols("RADLAN-JUMBOFRAMES-MIB", PYSNMP_MODULE_ID=rlJumboFrames, rlJumboFrames=rlJumboFrames, rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus, rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset)
