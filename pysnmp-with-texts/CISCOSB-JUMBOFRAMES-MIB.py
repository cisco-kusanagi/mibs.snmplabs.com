#
# PySNMP MIB module CISCOSB-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-JUMBOFRAMES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, iso, Counter32, NotificationType, Unsigned32, TimeTicks, Gauge32, MibIdentifier, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "iso", "Counter32", "NotificationType", "Unsigned32", "TimeTicks", "Gauge32", "MibIdentifier", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlJumboFrames.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlJumboFrames.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlJumboFrames.setDescription('This private MIB module defines Jumbo Frames private MIBs.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setDescription('Show the current Jumbo Frames status')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setDescription('Set the Jumbo Frames status after reset')
mibBuilder.exportSymbols("CISCOSB-JUMBOFRAMES-MIB", PYSNMP_MODULE_ID=rlJumboFrames, rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus, rlJumboFrames=rlJumboFrames, rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset)
