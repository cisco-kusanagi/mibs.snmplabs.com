#
# PySNMP MIB module TIMETRA-SAS-IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:14:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
dot1xAuthConfigEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthConfigEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, Integer32, IpAddress, NotificationType, Counter32, MibIdentifier, TimeTicks, Bits, ModuleIdentity, Counter64, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Integer32", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "ModuleIdentity", "Counter64", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
timetraSASNotifyPrefix, timetraSASObjs, timetraSASConfs, timetraSASModules = mibBuilder.importSymbols("TIMETRA-SAS-GLOBAL-MIB", "timetraSASNotifyPrefix", "timetraSASObjs", "timetraSASConfs", "timetraSASModules")
ServiceAdminStatus, TNamedItem, TPolicyStatementNameOrEmpty = mibBuilder.importSymbols("TIMETRA-TC-MIB", "ServiceAdminStatus", "TNamedItem", "TPolicyStatementNameOrEmpty")
timeraSASIEEE8021PaeMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 17))
timeraSASIEEE8021PaeMIBModule.setRevisions(('1912-07-01 00:00',))
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setLastUpdated('1207010000Z')
if mibBuilder.loadTexts: timeraSASIEEE8021PaeMIBModule.setOrganization('Alcatel-Lucent')
tmnxSASDot1xObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16))
tmnxSASDot1xAuthenticatorObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1))
tmnxSASDot1xConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12))
tmnxDot1xSASCompliancs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1))
tmnxDot1xSASGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2))
dot1xAuthConfigExtnTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1), )
if mibBuilder.loadTexts: dot1xAuthConfigExtnTable.setStatus('current')
dot1xAuthConfigExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1), )
dot1xAuthConfigEntry.registerAugmentions(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xAuthConfigExtnEntry"))
dot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
if mibBuilder.loadTexts: dot1xAuthConfigExtnEntry.setStatus('current')
dot1xPortEtherTunnel = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 16, 1, 1, 1, 150), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1xPortEtherTunnel.setStatus('current')
dot1xAuthConfigExtnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 2, 1)).setObjects(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xPortEtherTunnel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xAuthConfigExtnGroup = dot1xAuthConfigExtnGroup.setStatus('current')
dot1xAuthConfigExtnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 12, 1, 1)).setObjects(("TIMETRA-SAS-IEEE8021-PAE-MIB", "dot1xAuthConfigExtnGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1xAuthConfigExtnCompliance = dot1xAuthConfigExtnCompliance.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-SAS-IEEE8021-PAE-MIB", PYSNMP_MODULE_ID=timeraSASIEEE8021PaeMIBModule, timeraSASIEEE8021PaeMIBModule=timeraSASIEEE8021PaeMIBModule, tmnxSASDot1xAuthenticatorObjs=tmnxSASDot1xAuthenticatorObjs, dot1xAuthConfigExtnTable=dot1xAuthConfigExtnTable, dot1xAuthConfigExtnCompliance=dot1xAuthConfigExtnCompliance, tmnxDot1xSASCompliancs=tmnxDot1xSASCompliancs, tmnxDot1xSASGroups=tmnxDot1xSASGroups, tmnxSASDot1xObjs=tmnxSASDot1xObjs, dot1xPortEtherTunnel=dot1xPortEtherTunnel, dot1xAuthConfigExtnEntry=dot1xAuthConfigExtnEntry, tmnxSASDot1xConformance=tmnxSASDot1xConformance, dot1xAuthConfigExtnGroup=dot1xAuthConfigExtnGroup)
