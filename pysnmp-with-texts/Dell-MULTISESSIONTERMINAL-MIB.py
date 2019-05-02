#
# PySNMP MIB module Dell-MULTISESSIONTERMINAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-MULTISESSIONTERMINAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:56:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, Counter32, IpAddress, Integer32, ObjectIdentity, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Counter32", "IpAddress", "Integer32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "iso", "ModuleIdentity")
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
mibBuilder.exportSymbols("Dell-MULTISESSIONTERMINAL-MIB", PYSNMP_MODULE_ID=rlMultiSessionTerminal, rlTerminalDebugModePassword=rlTerminalDebugModePassword, rlMultiSessionTerminal=rlMultiSessionTerminal)
