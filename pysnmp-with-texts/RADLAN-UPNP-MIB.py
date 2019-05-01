#
# PySNMP MIB module RADLAN-UPNP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-UPNP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:50:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, Bits, iso, Integer32, Counter32, Counter64, ObjectIdentity, IpAddress, TimeTicks, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Bits", "iso", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "IpAddress", "TimeTicks", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlUPnP = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 109))
rlUPnP.setRevisions(('2006-03-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlUPnP.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlUPnP.setLastUpdated('200603260000Z')
if mibBuilder.loadTexts: rlUPnP.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlUPnP.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlUPnP.setDescription('The private MIB module definition for UPNP.')
rlUPnPUniqueDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 89, 109, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUPnPUniqueDeviceName.setStatus('current')
if mibBuilder.loadTexts: rlUPnPUniqueDeviceName.setDescription('The UDN (Unique Device Name) of the device.')
rlUPnPEnabling = MibScalar((1, 3, 6, 1, 4, 1, 89, 109, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUPnPEnabling.setStatus('current')
if mibBuilder.loadTexts: rlUPnPEnabling.setDescription('Indicates whether UPNP is enabled or disabled in the current device. The default state is device-dependent.')
mibBuilder.exportSymbols("RADLAN-UPNP-MIB", rlUPnP=rlUPnP, rlUPnPEnabling=rlUPnPEnabling, PYSNMP_MODULE_ID=rlUPnP, rlUPnPUniqueDeviceName=rlUPnPUniqueDeviceName)
