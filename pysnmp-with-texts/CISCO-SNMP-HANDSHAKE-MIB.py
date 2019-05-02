#
# PySNMP MIB module CISCO-SNMP-HANDSHAKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-HANDSHAKE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:12:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bsnWireless, = mibBuilder.importSymbols("AIRESPACE-WIRELESS-MIB", "bsnWireless")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32, NotificationType, Bits, Counter32, TimeTicks, ModuleIdentity, IpAddress, MibIdentifier, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32", "NotificationType", "Bits", "Counter32", "TimeTicks", "ModuleIdentity", "IpAddress", "MibIdentifier", "Integer32", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
ciscoSnmpHandshakeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179, 2, 40))
ciscoSnmpHandshakeMIB.setRevisions(('2007-05-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIB.setDescription('This MIB is intended for those devices where SNMP access is given to be given to known SNMP Manager only. All the SNMP MIBs are published, any thrid party SNMP browser can retrieve data using SNMP protocol. By implementing this MIB, a application layer handshake has to be done before any MIB view access is granted to SNMPV2c community string or SNMPV3 user. Once the handshake is successfully over then SNMP agent can create VACM entry to provide access to any MIB view. GLOSSARY View-based Access Control Model ( VACM ) The VACM determines whether access to a managed object in a local MIB by a remote SNMP manager should be allowed.')
ciscoSnmpHandshakeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 0))
ciscoSnmpHandshakeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1))
ciscoSnmpHandshakeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2))
ciscoSnmpHandshakeProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1))
ciscoSnmpHandshakeTest = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2))
csHandshakeInit = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeInit.setStatus('current')
if mibBuilder.loadTexts: csHandshakeInit.setDescription('Get on this object will return random 16 bytes octet-string. Device will cache this string against IP-Address of sender. This string will be later used to comeplete the handshake.')
csHandshakeUpdate = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csHandshakeUpdate.setStatus('current')
if mibBuilder.loadTexts: csHandshakeUpdate.setDescription("Set on this object will make snmp agent to run the secret algorithm to give access or deny access to SNMP manager. Access will be given to the community string used and to the sender's IP-Address only.")
csHandshakeCheck = MibScalar((1, 3, 6, 1, 4, 1, 14179, 2, 40, 1, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csHandshakeCheck.setStatus('current')
if mibBuilder.loadTexts: csHandshakeCheck.setDescription('This object can be use to perform test of MIB view access. Once the handshake is successfully completed. The MIB-view access will be granted for this object, If MIB-view is not granted yet for this object then no-access error will be returned.')
ciscoSnmpHandshakeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1))
ciscoSnmpHandshakeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2))
ciscoSnmpHandshakeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 1, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "ciscoSnmpHandshakeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeMIBCompliance = ciscoSnmpHandshakeMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpHandshakeMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoSnmpHandshakeMIB module.')
ciscoSnmpHandshakeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14179, 2, 40, 2, 2, 1)).setObjects(("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeInit"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeUpdate"), ("CISCO-SNMP-HANDSHAKE-MIB", "csHandshakeCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpHandshakeGroup = ciscoSnmpHandshakeGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpHandshakeGroup.setDescription('This collection of objects represents the information about attributes needed to completed SNMP handhshake')
mibBuilder.exportSymbols("CISCO-SNMP-HANDSHAKE-MIB", ciscoSnmpHandshakeMIB=ciscoSnmpHandshakeMIB, csHandshakeInit=csHandshakeInit, ciscoSnmpHandshakeProcess=ciscoSnmpHandshakeProcess, ciscoSnmpHandshakeMIBGroups=ciscoSnmpHandshakeMIBGroups, ciscoSnmpHandshakeMIBConform=ciscoSnmpHandshakeMIBConform, ciscoSnmpHandshakeMIBObjects=ciscoSnmpHandshakeMIBObjects, ciscoSnmpHandshakeMIBCompliances=ciscoSnmpHandshakeMIBCompliances, ciscoSnmpHandshakeTest=ciscoSnmpHandshakeTest, PYSNMP_MODULE_ID=ciscoSnmpHandshakeMIB, ciscoSnmpHandshakeMIBNotifs=ciscoSnmpHandshakeMIBNotifs, ciscoSnmpHandshakeGroup=ciscoSnmpHandshakeGroup, csHandshakeUpdate=csHandshakeUpdate, csHandshakeCheck=csHandshakeCheck, ciscoSnmpHandshakeMIBCompliance=ciscoSnmpHandshakeMIBCompliance)
