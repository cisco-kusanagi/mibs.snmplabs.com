#
# PySNMP MIB module ACMEPACKET-PRODUCTS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ACMEPACKET-PRODUCTS
# Produced by pysmi-0.3.4 at Wed May  1 11:13:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacket, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacket")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, NotificationType, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, MibIdentifier, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "NotificationType", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "MibIdentifier", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acmepacketProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 1))
acmepacketProducts.setRevisions(('2012-07-16 00:00', '2007-04-03 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acmepacketProducts.setRevisionsDescriptions(('Updated contact info', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: acmepacketProducts.setLastUpdated('201207160000Z')
if mibBuilder.loadTexts: acmepacketProducts.setOrganization('Acme Packet, Inc.')
if mibBuilder.loadTexts: acmepacketProducts.setContactInfo(' Customer Service Postal: Acme Packet, Inc 100 Crosby Drive Bedford, MA 01730 US Tel: 1-781-328-4400 E-mail: support@acmepacket.com')
if mibBuilder.loadTexts: acmepacketProducts.setDescription('Products supported at Acme Packet.')
apNetNet4000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 1))
if mibBuilder.loadTexts: apNetNet4000Series.setStatus('current')
if mibBuilder.loadTexts: apNetNet4000Series.setDescription('This is subtree contains all product lines supported in the Net-Net 4000 Series product line.')
apNetNet4250 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 1, 1))
if mibBuilder.loadTexts: apNetNet4250.setStatus('current')
if mibBuilder.loadTexts: apNetNet4250.setDescription('The Net-Net 4250 product.')
apNetNet4500 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 1, 2))
if mibBuilder.loadTexts: apNetNet4500.setStatus('current')
if mibBuilder.loadTexts: apNetNet4500.setDescription('The Net-Net 4500 product.')
apNetNet9000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 2))
if mibBuilder.loadTexts: apNetNet9000Series.setStatus('current')
if mibBuilder.loadTexts: apNetNet9000Series.setDescription('This is subtree contains all product lines supported in the Net-Net 9000 Series product line.')
apNetNet9200 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 2, 1))
if mibBuilder.loadTexts: apNetNet9200.setStatus('current')
if mibBuilder.loadTexts: apNetNet9200.setDescription('The Net-Net 9200 product.')
apNetNet3000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 3))
if mibBuilder.loadTexts: apNetNet3000Series.setStatus('current')
if mibBuilder.loadTexts: apNetNet3000Series.setDescription('This is subtree contains all product lines supported in the Net-Net 3000 Series product line.')
apNetNet3800 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 3, 1))
if mibBuilder.loadTexts: apNetNet3800.setStatus('current')
if mibBuilder.loadTexts: apNetNet3800.setDescription('The Net-Net 3800 product.')
apNetNet3820 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 3, 2))
if mibBuilder.loadTexts: apNetNet3820.setStatus('current')
if mibBuilder.loadTexts: apNetNet3820.setDescription('The Net-Net 3820 product.')
apNetNetOSSeries = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 4))
if mibBuilder.loadTexts: apNetNetOSSeries.setStatus('current')
if mibBuilder.loadTexts: apNetNetOSSeries.setDescription('This is subtree contains all product lines supported in the Net-Net OS Series product line.')
apNetNetOS = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 4, 1))
if mibBuilder.loadTexts: apNetNetOS.setStatus('current')
if mibBuilder.loadTexts: apNetNetOS.setDescription('The Net-Net OS running on third party hardware.')
apNetNetOSVM = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 4, 2))
if mibBuilder.loadTexts: apNetNetOSVM.setStatus('current')
if mibBuilder.loadTexts: apNetNetOSVM.setDescription('The Net-Net OS running in a virtual machine environment.')
apNetNet6000Series = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 5))
if mibBuilder.loadTexts: apNetNet6000Series.setStatus('current')
if mibBuilder.loadTexts: apNetNet6000Series.setDescription('This is subtree contains all product lines supported in the Net-Net 6000 Series product line.')
apNetNet6300 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9148, 1, 5, 1))
if mibBuilder.loadTexts: apNetNet6300.setStatus('current')
if mibBuilder.loadTexts: apNetNet6300.setDescription('The Net-Net 6300 product.')
mibBuilder.exportSymbols("ACMEPACKET-PRODUCTS", apNetNet6000Series=apNetNet6000Series, apNetNet9000Series=apNetNet9000Series, apNetNet3820=apNetNet3820, PYSNMP_MODULE_ID=acmepacketProducts, apNetNetOSVM=apNetNetOSVM, acmepacketProducts=acmepacketProducts, apNetNet4500=apNetNet4500, apNetNet3800=apNetNet3800, apNetNet3000Series=apNetNet3000Series, apNetNet9200=apNetNet9200, apNetNet4000Series=apNetNet4000Series, apNetNet4250=apNetNet4250, apNetNetOSSeries=apNetNetOSSeries, apNetNetOS=apNetNetOS, apNetNet6300=apNetNet6300)