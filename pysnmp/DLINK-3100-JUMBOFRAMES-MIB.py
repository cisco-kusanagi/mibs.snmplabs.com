#
# PySNMP MIB module DLINK-3100-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-JUMBOFRAMES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Gauge32, IpAddress, Unsigned32, MibIdentifier, Integer32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Gauge32", "IpAddress", "Unsigned32", "MibIdentifier", "Integer32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "NotificationType", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-JUMBOFRAMES-MIB", rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset, PYSNMP_MODULE_ID=rlJumboFrames, rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus, rlJumboFrames=rlJumboFrames)
