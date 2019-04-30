#
# PySNMP MIB module RADLAN-UPNP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-UPNP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:41:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, ObjectIdentity, Counter64, Unsigned32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, IpAddress, Bits, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Counter64", "Unsigned32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "IpAddress", "Bits", "iso", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlUPnP = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 109))
rlUPnP.setRevisions(('2006-03-26 00:00',))
if mibBuilder.loadTexts: rlUPnP.setLastUpdated('200603260000Z')
if mibBuilder.loadTexts: rlUPnP.setOrganization('Radlan Computer Communications Ltd.')
rlUPnPUniqueDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 89, 109, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUPnPUniqueDeviceName.setStatus('current')
rlUPnPEnabling = MibScalar((1, 3, 6, 1, 4, 1, 89, 109, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUPnPEnabling.setStatus('current')
mibBuilder.exportSymbols("RADLAN-UPNP-MIB", rlUPnPUniqueDeviceName=rlUPnPUniqueDeviceName, rlUPnP=rlUPnP, PYSNMP_MODULE_ID=rlUPnP, rlUPnPEnabling=rlUPnPEnabling)
