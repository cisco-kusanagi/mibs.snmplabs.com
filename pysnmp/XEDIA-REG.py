#
# PySNMP MIB module XEDIA-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-REG
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Gauge32, ModuleIdentity, Bits, NotificationType, IpAddress, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, iso, Counter64, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "ModuleIdentity", "Bits", "NotificationType", "IpAddress", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "iso", "Counter64", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xedia = ObjectIdentity((1, 3, 6, 1, 4, 1, 838))
if mibBuilder.loadTexts: xedia.setStatus('current')
xediaRegistrations = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 2))
if mibBuilder.loadTexts: xediaRegistrations.setLastUpdated('9612202155Z')
if mibBuilder.loadTexts: xediaRegistrations.setOrganization('Xedia Corp.')
xediaMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 3))
if mibBuilder.loadTexts: xediaMibs.setStatus('current')
xediaClasses = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 4))
if mibBuilder.loadTexts: xediaClasses.setStatus('current')
xediaProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 5))
if mibBuilder.loadTexts: xediaProducts.setStatus('current')
xediaAccessView = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 6))
if mibBuilder.loadTexts: xediaAccessView.setStatus('current')
xediaQvpnBuilder = ObjectIdentity((1, 3, 6, 1, 4, 1, 838, 6, 1))
if mibBuilder.loadTexts: xediaQvpnBuilder.setStatus('current')
class LongDisplayString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2048)

mibBuilder.exportSymbols("XEDIA-REG", xediaAccessView=xediaAccessView, xediaMibs=xediaMibs, LongDisplayString=LongDisplayString, PYSNMP_MODULE_ID=xediaRegistrations, xediaQvpnBuilder=xediaQvpnBuilder, xedia=xedia, xediaRegistrations=xediaRegistrations, xediaClasses=xediaClasses, xediaProducts=xediaProducts)
