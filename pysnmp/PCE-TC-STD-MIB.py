#
# PySNMP MIB module PCE-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCE-TC-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, experimental, iso, Gauge32, Bits, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "experimental", "iso", "Gauge32", "Bits", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pceTCDraftMIB = ModuleIdentity((1, 3, 6, 1, 3, 9999, 1))
if mibBuilder.loadTexts: pceTCDraftMIB.setLastUpdated('200709250000Z')
if mibBuilder.loadTexts: pceTCDraftMIB.setOrganization('Path Computation Element (PCE) Working Group')
pceStdMIB = MibIdentifier((1, 3, 6, 1, 3, 9999))
class PcePcepIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d:1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 6)

class PceRoutingDomainID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

mibBuilder.exportSymbols("PCE-TC-STD-MIB", pceTCDraftMIB=pceTCDraftMIB, PYSNMP_MODULE_ID=pceTCDraftMIB, PcePcepIdentifier=PcePcepIdentifier, pceStdMIB=pceStdMIB, PceRoutingDomainID=PceRoutingDomainID)
