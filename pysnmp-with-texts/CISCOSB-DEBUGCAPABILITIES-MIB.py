#
# PySNMP MIB module CISCOSB-DEBUGCAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-DEBUGCAPABILITIES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, NotificationType, iso, TimeTicks, IpAddress, Gauge32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "NotificationType", "iso", "TimeTicks", "IpAddress", "Gauge32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDebugCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 206))
rlDebugCapabilities.setRevisions(('2011-01-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDebugCapabilities.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDebugCapabilities.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlDebugCapabilities.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlDebugCapabilities.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlDebugCapabilities.setDescription('This private MIB module is used for achieving extended debugging capablities for the device. For example: greater management capabilies for technical support users.')
rlDebugCapabilitiesPassword = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 206, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setStatus('current')
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setDescription('A user intereseted to obtain extended debug capabilities should SET this MIB to a well known secret value (it is intended to be used only by authorized users). Most often, this value will be based on the device MAC address. Upon setting the correct value, the SET operation will return noError. Otherwise, wrongValue will return to the caller. GET operation on this MIB will reurn a value of length 0.')
mibBuilder.exportSymbols("CISCOSB-DEBUGCAPABILITIES-MIB", PYSNMP_MODULE_ID=rlDebugCapabilities, rlDebugCapabilitiesPassword=rlDebugCapabilitiesPassword, rlDebugCapabilities=rlDebugCapabilities)
