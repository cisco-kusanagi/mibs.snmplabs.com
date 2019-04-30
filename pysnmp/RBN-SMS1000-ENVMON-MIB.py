#
# PySNMP MIB module RBN-SMS1000-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-SMS1000-ENVMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:44:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, IpAddress, Gauge32, MibIdentifier, Integer32, Counter32, ModuleIdentity, Counter64, iso, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Gauge32", "MibIdentifier", "Integer32", "Counter32", "ModuleIdentity", "Counter64", "iso", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rbnSMS1000EnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 3))
if mibBuilder.loadTexts: rbnSMS1000EnvMonMIB.setLastUpdated('9810062300Z')
if mibBuilder.loadTexts: rbnSMS1000EnvMonMIB.setOrganization('RedBack Networks, Inc.')
rbnSMS1000EnvMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 3, 0))
rbnSMS1000EnvMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 3, 1))
rbnSMS1000EnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 3, 2))
rbnSMS1000FanFail = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 3, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSMS1000FanFail.setStatus('current')
rbnSMS1000PowerFail = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnSMS1000PowerFail.setStatus('current')
rbnSMS1000FanFailChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 3, 0, 1)).setObjects(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000FanFail"))
if mibBuilder.loadTexts: rbnSMS1000FanFailChange.setStatus('current')
rbnSMS1000PowerFailChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 3, 0, 2)).setObjects(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000PowerFail"))
if mibBuilder.loadTexts: rbnSMS1000PowerFailChange.setStatus('current')
rbnSMS1000EnvMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 1))
rbnSMS1000EnvMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 2))
rbnSMS1000EnvMonMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 1, 1)).setObjects(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000FanFail"), ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000PowerFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSMS1000EnvMonMIBObjectGroup = rbnSMS1000EnvMonMIBObjectGroup.setStatus('current')
rbnSMS1000EnvMonMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 1, 2)).setObjects(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000FanFailChange"), ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000PowerFailChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSMS1000EnvMonMIBNotificationGroup = rbnSMS1000EnvMonMIBNotificationGroup.setStatus('current')
rbnSMS1000EnvMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 3, 2, 2, 1)).setObjects(("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000EnvMonMIBObjectGroup"), ("RBN-SMS1000-ENVMON-MIB", "rbnSMS1000EnvMonMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnSMS1000EnvMonMIBCompliance = rbnSMS1000EnvMonMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("RBN-SMS1000-ENVMON-MIB", rbnSMS1000EnvMonMIBNotifications=rbnSMS1000EnvMonMIBNotifications, PYSNMP_MODULE_ID=rbnSMS1000EnvMonMIB, rbnSMS1000EnvMonMIBCompliance=rbnSMS1000EnvMonMIBCompliance, rbnSMS1000FanFail=rbnSMS1000FanFail, rbnSMS1000EnvMonMIBGroups=rbnSMS1000EnvMonMIBGroups, rbnSMS1000EnvMonMIBNotificationGroup=rbnSMS1000EnvMonMIBNotificationGroup, rbnSMS1000EnvMonMIBObjectGroup=rbnSMS1000EnvMonMIBObjectGroup, rbnSMS1000EnvMonMIB=rbnSMS1000EnvMonMIB, rbnSMS1000EnvMonMIBConformance=rbnSMS1000EnvMonMIBConformance, rbnSMS1000FanFailChange=rbnSMS1000FanFailChange, rbnSMS1000EnvMonMIBCompliances=rbnSMS1000EnvMonMIBCompliances, rbnSMS1000PowerFailChange=rbnSMS1000PowerFailChange, rbnSMS1000PowerFail=rbnSMS1000PowerFail, rbnSMS1000EnvMonMIBObjects=rbnSMS1000EnvMonMIBObjects)
