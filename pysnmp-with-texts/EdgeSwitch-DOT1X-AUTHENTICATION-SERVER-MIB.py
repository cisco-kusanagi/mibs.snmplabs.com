#
# PySNMP MIB module EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:10:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ObjectIdentity, NotificationType, iso, Counter32, ModuleIdentity, Gauge32, MibIdentifier, Integer32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ObjectIdentity", "NotificationType", "iso", "Counter32", "ModuleIdentity", "Gauge32", "MibIdentifier", "Integer32", "TimeTicks", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
fastPathdot1xAuthenticationServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49))
fastPathdot1xAuthenticationServer.setRevisions(('2011-01-26 00:00', '2009-11-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathdot1xAuthenticationServer.setRevisionsDescriptions(('Postal address updated.', 'Ubiquiti branding related changes.',))
if mibBuilder.loadTexts: fastPathdot1xAuthenticationServer.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathdot1xAuthenticationServer.setOrganization('Broadcom Inc')
if mibBuilder.loadTexts: fastPathdot1xAuthenticationServer.setContactInfo('')
if mibBuilder.loadTexts: fastPathdot1xAuthenticationServer.setDescription('The Ubiquiti Private MIB for FastPath Dot1x Authentication Server ')
agentDot1xAuthServUserConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1))
agentDot1xAuthServUserConfigCreate = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigCreate.setStatus('current')
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigCreate.setDescription("Create a new user. When set with a non-empty string, a new user with that name will be created. This object will only return an empty string. This string is limited to alpha-numeric strings (including the '-' and '_' characters).")
agentDot1xAuthServUserConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2), )
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigTable.setDescription('A table for dot1x Client details and associated functionality.')
agentDot1xAuthServUserConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1), ).setIndexNames((0, "EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB", "agentDot1xAuthServUserIndex"))
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentDot1xAuthServUserConfigEntry.setDescription('Represents entry for port config table.')
agentDot1xAuthServUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99)))
if mibBuilder.loadTexts: agentDot1xAuthServUserIndex.setStatus('current')
if mibBuilder.loadTexts: agentDot1xAuthServUserIndex.setDescription('Dot1x user config index. ')
agentDot1xAuthServUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserName.setStatus('current')
if mibBuilder.loadTexts: agentDot1xAuthServUserName.setDescription("Dot1x user name. This string is limited to alpha-numeric strings (including '-' and '_' characters). ")
agentDot1xAuthServUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserPassword.setStatus('current')
if mibBuilder.loadTexts: agentDot1xAuthServUserPassword.setDescription('Dot1x user password.')
agentDot1xAuthServUserStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 49, 1, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentDot1xAuthServUserStatus.setStatus('current')
if mibBuilder.loadTexts: agentDot1xAuthServUserStatus.setDescription('Dot1x User Status. active(1) - This user account is active. destroy(6) - Set to this value to remove this user account.')
mibBuilder.exportSymbols("EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB", agentDot1xAuthServUserStatus=agentDot1xAuthServUserStatus, agentDot1xAuthServUserName=agentDot1xAuthServUserName, fastPathdot1xAuthenticationServer=fastPathdot1xAuthenticationServer, agentDot1xAuthServUserConfigGroup=agentDot1xAuthServUserConfigGroup, agentDot1xAuthServUserConfigCreate=agentDot1xAuthServUserConfigCreate, agentDot1xAuthServUserConfigEntry=agentDot1xAuthServUserConfigEntry, PYSNMP_MODULE_ID=fastPathdot1xAuthenticationServer, agentDot1xAuthServUserConfigTable=agentDot1xAuthServUserConfigTable, agentDot1xAuthServUserPassword=agentDot1xAuthServUserPassword, agentDot1xAuthServUserIndex=agentDot1xAuthServUserIndex)
