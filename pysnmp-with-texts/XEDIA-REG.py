#
# PySNMP MIB module XEDIA-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-REG
# Produced by pysmi-0.3.4 at Wed May  1 15:42:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, Gauge32, NotificationType, Counter32, MibIdentifier, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, enterprises, ModuleIdentity, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Gauge32", "NotificationType", "Counter32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "enterprises", "ModuleIdentity", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xedia = ObjectIdentity((1, 3, 6, 1, 4, 1, 838))
if mibBuilder.loadTexts: xedia.setStatus('current')
if mibBuilder.loadTexts: xedia.setDescription("Xedia's node in the naming hierarchy as assigned by the Internet Assigned Numbers Authority (IANA).")
xediaRegistrations = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 2))
if mibBuilder.loadTexts: xediaRegistrations.setLastUpdated('9612202155Z')
if mibBuilder.loadTexts: xediaRegistrations.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaRegistrations.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaRegistrations.setDescription('This module defines the enterprises OID of Xedia and other company-wide definitions. The resulting top-level name space under the xedia branch looks like this: xedia (agentConfig - an older MIB defined for MADswitch) xediaRegistrations - this module xediaMibs - MIB modules defined in .mi2 files xediaClasses - CLASS modules defined .mo files xediaProducts - AGENT-CAPABILITIES modules defined in .mi2 files This is where you reserve an OIDs for a MIB module. The values are defined in the appropriate .mi2/.mo files but are in comments here so that we can have one document under source control to reserve and catalog values.')
xediaMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 3))
if mibBuilder.loadTexts: xediaMibs.setStatus('current')
if mibBuilder.loadTexts: xediaMibs.setDescription('A registration point under which all (new) Xedia MIB modules are defined.')
xediaClasses = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 4))
if mibBuilder.loadTexts: xediaClasses.setStatus('current')
if mibBuilder.loadTexts: xediaClasses.setDescription('A registration point under which all Xedia CLASS definition modules are defined.')
xediaProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 5))
if mibBuilder.loadTexts: xediaProducts.setStatus('current')
if mibBuilder.loadTexts: xediaProducts.setDescription('A registration point under which all Xedia AGENT-CAPABILITIES definitions (and therefore values of sysObjectId) are defined.')
xediaAccessView = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 6))
if mibBuilder.loadTexts: xediaAccessView.setStatus('current')
if mibBuilder.loadTexts: xediaAccessView.setDescription('A registration point for Xedia Network Management Products and mib definitions.')
xediaQvpnBuilder = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 6, 1))
if mibBuilder.loadTexts: xediaQvpnBuilder.setStatus('current')
if mibBuilder.loadTexts: xediaQvpnBuilder.setDescription('A registration point for Xedia QVPN Builder.')
class LongDisplayString(TextualConvention, OctetString):
    description = 'A string that has the same properties as a DisplayString except it can be up to 2048 characters long.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

mibBuilder.exportSymbols("XEDIA-REG", xediaQvpnBuilder=xediaQvpnBuilder, LongDisplayString=LongDisplayString, xediaProducts=xediaProducts, xediaAccessView=xediaAccessView, xediaRegistrations=xediaRegistrations, xediaMibs=xediaMibs, xedia=xedia, PYSNMP_MODULE_ID=xediaRegistrations, xediaClasses=xediaClasses)
