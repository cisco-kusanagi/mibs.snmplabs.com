#
# PySNMP MIB module Dell-VRTX-MULTISESSIONTERMINAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-VRTX-MULTISESSIONTERMINAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:57:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("Dell-VRTX-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, Unsigned32, iso, ObjectIdentity, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, IpAddress, Integer32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Unsigned32", "iso", "ObjectIdentity", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "IpAddress", "Integer32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlMultiSessionTerminal = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 69))
rlMultiSessionTerminal.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlMultiSessionTerminal.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlMultiSessionTerminal.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setOrganization('Dell')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlMultiSessionTerminal.setDescription('This private MIB module defines Multi Session Terminal private MIBs.')
rlTerminalDebugModePassword = MibScalar((1, 3, 6, 1, 4, 1, 89, 69, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTerminalDebugModePassword.setStatus('current')
if mibBuilder.loadTexts: rlTerminalDebugModePassword.setDescription('When a user wants to change the terminal mode from debug mode to ASCII he must enter this password first')
mibBuilder.exportSymbols("Dell-VRTX-MULTISESSIONTERMINAL-MIB", rlMultiSessionTerminal=rlMultiSessionTerminal, rlTerminalDebugModePassword=rlTerminalDebugModePassword, PYSNMP_MODULE_ID=rlMultiSessionTerminal)
