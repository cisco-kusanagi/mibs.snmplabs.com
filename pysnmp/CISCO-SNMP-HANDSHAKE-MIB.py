#
# PySNMP MIB module CISCO-SNMP-HANDSHAKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-HANDSHAKE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsnWireless, = mibBuilder.importSymbols("AIRESPACE-WIRELESS-MIB", "bsnWireless")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, iso, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter64, Gauge32, Bits, ObjectIdentity, Integer32, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter64", "Gauge32", "Bits", "ObjectIdentity", "Integer32", "TimeTicks", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoSnmpHandshakeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179, 2, 40))
ciscoSnmpHandshakeMIB.setRevisions(('2007-05-23 00:00',))
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setOrganization('Cisco Systems Inc.')
ciscoSnmpHandshakeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 0))
ciscoSnmpHandshakeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1))
ciscoSnmpHandshakeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2))
ciscoSnmpHandshakeProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1))
ciscoSnmpHandshakeTest = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2))
csHandshakeInit = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeInit.setStatus('current')
csHandshakeUpdate = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csHandshakeUpdate.setStatus('current')
csHandshakeCheck = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeCheck.setStatus('current')
ciscoSnmpHandshakeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1))
ciscoSnmpHandshakeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2))
ciscoSnmpHandshakeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "ciscoSnmpHandshakeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeMIBCompliance = ciscoSnmpHandshakeMIBCompliance.setStatus('current')
ciscoSnmpHandshakeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeInit"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeUpdate"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeGroup = ciscoSnmpHandshakeGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-HANDSHAKE-MIB", csHandshakeInit=csHandshakeInit, csHandshakeCheck=csHandshakeCheck, PYSNMP_MODULE_ID=ciscoSnmpHandshakeMIB, ciscoSnmpHandshakeMIBObjects=ciscoSnmpHandshakeMIBObjects, ciscoSnmpHandshakeMIB=ciscoSnmpHandshakeMIB, ciscoSnmpHandshakeTest=ciscoSnmpHandshakeTest, ciscoSnmpHandshakeMIBGroups=ciscoSnmpHandshakeMIBGroups, ciscoSnmpHandshakeMIBCompliance=ciscoSnmpHandshakeMIBCompliance, ciscoSnmpHandshakeMIBCompliances=ciscoSnmpHandshakeMIBCompliances, ciscoSnmpHandshakeGroup=ciscoSnmpHandshakeGroup, ciscoSnmpHandshakeMIBConform=ciscoSnmpHandshakeMIBConform, ciscoSnmpHandshakeMIBNotifs=ciscoSnmpHandshakeMIBNotifs, csHandshakeUpdate=csHandshakeUpdate, ciscoSnmpHandshakeProcess=ciscoSnmpHandshakeProcess)
