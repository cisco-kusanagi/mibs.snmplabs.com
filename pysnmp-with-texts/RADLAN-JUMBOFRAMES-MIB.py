#
# PySNMP MIB module RADLAN-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-JUMBOFRAMES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:47:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Counter32, ObjectIdentity, Counter64, Integer32, MibIdentifier, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Counter32", "ObjectIdentity", "Counter64", "Integer32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlJumboFrames.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlJumboFrames.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlJumboFrames.setDescription('This private MIB module defines Jumbo Frames private MIBs.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setDescription('Show the current Jumbo Frames status')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setDescription('Set the Jumbo Frames status after reset')
mibBuilder.exportSymbols("RADLAN-JUMBOFRAMES-MIB", rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus, rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset, rlJumboFrames=rlJumboFrames, PYSNMP_MODULE_ID=rlJumboFrames)
